#!/usr/bin/env python3

"""
MinIO Migration Script

This script migrates objects from one MinIO bucket to another, with support for:
- Moving objects between different MinIO instances
- Moving or copying objects (with --move flag)
- Preserving all object metadata (content type, custom headers, etc.)
- Dry run mode to preview changes
- Automatic bucket creation if destination doesn't exist
- Organizing objects into folders based on filename length

Usage examples:
1. Copy between buckets on same instance:
   python minio_migrate.py --source-access-key KEY1 --source-secret-key SECRET1 --source-bucket old --dest-bucket new

2. Move between different MinIO instances:
   python minio_migrate.py --source-host host1:9000 --source-access-key KEY1 --source-secret-key SECRET1 \
                          --dest-host host2:9000 --dest-access-key KEY2 --dest-secret-key SECRET2 \
                          --source-bucket old --dest-bucket new --move

3. Dry run to preview changes:
   python minio_migrate.py --source-access-key KEY --source-secret-key SECRET --dry-run
"""

from minio import Minio
from minio.error import S3Error
from argparse import ArgumentParser, Namespace
from io import BytesIO


def get_args() -> Namespace:
    parser = ArgumentParser(description="Migrate objects from one Minio bucket to another")
    
    # Source MinIO instance
    parser.add_argument("--source-host", default="localhost:9000", help="Source Minio server address")
    parser.add_argument("--source-secure", action='store_true', help="Use HTTPS for source Minio server")
    parser.add_argument("--source-access-key", required=True, help="Source Minio access key")
    parser.add_argument("--source-secret-key", required=True, help="Source Minio secret key")
    parser.add_argument("--source-bucket", default="default", help="Source bucket name")
    
    # Destination MinIO instance
    parser.add_argument("--dest-host", help="Destination Minio server address (defaults to source host)")
    parser.add_argument("--dest-secure", action='store_true', help="Use HTTPS for destination Minio server")
    parser.add_argument("--dest-access-key", help="Destination Minio access key (defaults to source key)")
    parser.add_argument("--dest-secret-key", help="Destination Minio secret key (defaults to source key)")
    parser.add_argument("--dest-bucket", default="newbucket", help="Destination bucket name")
    
    # Migration options
    parser.add_argument("--move", action='store_true', help="Move objects (delete from source after copy)")
    parser.add_argument("--dry-run", action='store_true', help="Show what would be done without actually doing it")
    
    return parser.parse_args()


def main():
    args = get_args()
    
    # Set defaults for destination if not provided
    dest_host = args.dest_host or args.source_host
    dest_access_key = args.dest_access_key or args.source_access_key
    dest_secret_key = args.dest_secret_key or args.source_secret_key
    
    # Create source MinIO client
    source_client = Minio(
        args.source_host,
        access_key=args.source_access_key,
        secret_key=args.source_secret_key,
        secure=args.source_secure,
    )
    
    # Create destination MinIO client
    dest_client = Minio(
        dest_host,
        access_key=dest_access_key,
        secret_key=dest_secret_key,
        secure=args.dest_secure,
    )

    source_bucket = args.source_bucket
    dest_bucket = args.dest_bucket

    # Check if destination bucket exists
    dest_exists = dest_client.bucket_exists(dest_bucket)
    print(f"Destination bucket '{dest_bucket}' exists: {dest_exists}")
    
    if not dest_exists:
        if args.dry_run:
            print(f"[DRY RUN] Would create destination bucket '{dest_bucket}'")
        else:
            dest_client.make_bucket(dest_bucket)
            print(f"Created destination bucket '{dest_bucket}'")

    # Check if source bucket exists
    if not source_client.bucket_exists(source_bucket):
        print(f"Error: Source bucket '{source_bucket}' does not exist")
        return

    objects = source_client.list_objects(source_bucket, prefix="", recursive=False)
    total_objects = 0
    copied_objects = 0
    failed_objects = 0
    
    for obj in objects:
        total_objects += 1
        name = obj.object_name
        if name is None:
            print("Warning: Object name is None, skipping.")
            failed_objects += 1
            continue
            
        if '/' in name:  # skip files already in folders
            print(f"Skipping {name} (already in a folder)")
            continue
            
        # Decide target folder inside dest_bucket
        if len(name) == 16:
            target = f"resources/{name}"
        else:
            target = f"attachments/{name}"
            
        try:
            if args.dry_run:
                # Get object metadata for dry run info
                obj_stat = source_client.stat_object(source_bucket, name)
                metadata_count = len(obj_stat.metadata) if obj_stat.metadata else 0
                metadata_info = f" (preserving {metadata_count} metadata fields)" if metadata_count > 0 else " (no metadata)"
                
                print(f"[DRY RUN] Would copy {name} to {dest_bucket}/{target}{metadata_info}")
                if args.move:
                    print(f"[DRY RUN] Would delete {name} from {source_bucket}")
            else:
                # Get object metadata first
                obj_stat = source_client.stat_object(source_bucket, name)
                
                # Get object from source
                response = source_client.get_object(source_bucket, name)
                
                # Read the data from response
                data = response.read()
                response.close()
                
                # Preserve all metadata - convert to proper format for MinIO
                metadata = None
                if obj_stat.metadata:
                    # Convert metadata to the format expected by MinIO
                    metadata = {}
                    if hasattr(obj_stat.metadata, 'items'):
                        for key, value in obj_stat.metadata.items():
                            # Ensure values are in the correct format (str, List[str], or Tuple[str])
                            if isinstance(value, (list, tuple)):
                                metadata[key] = value
                            else:
                                metadata[key] = str(value)
                    elif isinstance(obj_stat.metadata, dict):
                        for key, value in obj_stat.metadata.items():
                            if isinstance(value, (list, tuple)):
                                metadata[key] = value
                            else:
                                metadata[key] = str(value)
                
                content_type = obj_stat.content_type or 'application/octet-stream'
                
                # Upload to destination with preserved metadata
                put_args = {
                    'bucket_name': dest_bucket,
                    'object_name': target,
                    'data': BytesIO(data),
                    'length': len(data),
                    'content_type': content_type
                }
                if metadata:
                    put_args['metadata'] = metadata
                
                dest_client.put_object(**put_args)
                
                # Log what was copied with metadata info
                metadata_info = f" (with {len(metadata)} metadata fields)" if metadata else " (no metadata)"
                print(f"Copied {name} to {dest_bucket}/{target}{metadata_info}")
                copied_objects += 1
                
                # If move operation, delete from source
                if args.move:
                    source_client.remove_object(source_bucket, name)
                    print(f"Deleted {name} from {source_bucket}")
                    
        except S3Error as err:
            print(f"Error processing {name}: {err}")
            failed_objects += 1
        except Exception as err:
            print(f"Unexpected error processing {name}: {err}")
            failed_objects += 1
    
    # Print summary
    print(f"\nMigration summary:")
    print(f"Total objects processed: {total_objects}")
    if not args.dry_run:
        print(f"Successfully copied: {copied_objects}")
        print(f"Failed: {failed_objects}")
        if args.move:
            print(f"Operation: MOVE (objects deleted from source)")
        else:
            print(f"Operation: COPY (objects remain in source)")
    else:
        print("DRY RUN - No actual changes made")


if __name__ == "__main__":
    main()
