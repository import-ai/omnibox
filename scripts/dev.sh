#!/usr/bin/env bash

function compose() {
    grep -v 'PWD' compose/deps.yaml > compose/tmp.yaml
    local cmd_args=("docker" "compose" "-f" "compose.yaml" "-f" "compose/tmp.yaml" "-f" "compose/dev.yaml")

    if [ -f "compose.override.yaml" ]; then
        cmd_args+=("-f" "compose.override.yaml")
    fi

    "${cmd_args[@]}" "$@"
}

compose "$@"
