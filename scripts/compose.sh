#!/usr/bin/env bash

TMPDIR=$(mktemp -d)
trap 'rm -rf "${TMPDIR}"' EXIT

function compose() {
    for file in compose/compose.*.yaml; do
        if [[ -f "$file" ]]; then
            grep "$file" -v 'PWD' > "${TMPDIR}/$(basename "$file")"
        fi
    done
    grep -v 'PWD' compose.yaml > "${TMPDIR}/compose.tmp.yaml"
    docker compose -f "${TMPDIR}/compose.tmp.yaml" -f /compose/compose.dev.yaml "$@"
}

compose "$@"
