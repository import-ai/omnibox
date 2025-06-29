#!/usr/bin/env python3
import re
import sys


def load_env_vars(env_path):
    env_vars = set()
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            m = re.match(r'^([A-Za-z_][A-Za-z0-9_]+)\s*=', line)
            if m:
                env_vars.add(m.group(1))
    return env_vars


def load_docker_compose_vars(compose_path):
    compose_vars = set()
    with open(compose_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Match ${VAR} or ${VAR:-default}
            matches = re.findall(r'\${([A-Za-z_][A-Za-z0-9_]*)(?::-?[^}]*)?}', line)
            # Match $VAR but $$VAR excluded
            matches += [m for m in re.findall(r'\$(\w+)', line) if not line.strip().startswith('$$')]
            compose_vars.update(matches)
    return compose_vars


def load_vars_from_file(file_path):
    if file_path.endswith('.env'):
        return load_env_vars(file_path)
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return load_docker_compose_vars(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}.")


def main():
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <first_file> <second_file>")
        sys.exit(1)
    first_vars = load_vars_from_file(sys.argv[1])
    second_vars = load_vars_from_file(sys.argv[2])
    first_only = sorted(first_vars - second_vars)
    second_only = sorted(second_vars - first_vars)
    if first_only or second_only:
        if first_only:
            print(f"Variables only in {sys.argv[1]}:")
            for var in first_only:
                print(var)
        else:
            print(f"Variables only in {sys.argv[2]}:")
            for var in second_only:
                print(var)
    else:
        print("No differences found.")

if __name__ == '__main__':
    main()
