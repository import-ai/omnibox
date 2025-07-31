#!/usr/bin/env bash

function compose() {
    local cmd_args=("docker" "compose" "-f" "compose.yaml" "-f" "compose/deps.yaml")

    if [ -f "compose.override.yaml" ]; then
        cmd_args+=("-f" "compose.override.yaml")
    fi

    "${cmd_args[@]}" "$@"
}

compose "$@"
