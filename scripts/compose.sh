#!/usr/bin/env bash

function compose() {
    docker compose -f compose.yaml -f compose/deps.yaml "$@"
}

compose "$@"
