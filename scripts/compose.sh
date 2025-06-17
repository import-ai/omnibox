#!/usr/bin/env bash

function compose() {
    grep -v 'PWD' compose.yaml > compose.tmp.yaml
    docker compose -f compose.tmp.yaml -f compose.dev.yaml "$@"
}

compose "$@"
