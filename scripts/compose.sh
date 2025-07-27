#!/usr/bin/env bash

function compose() {
    grep -v 'PWD' depends.compose.yaml > compose.tmp.yaml
    docker compose -f compose.yaml -f compose.tmp.yaml -f compose.dev.yaml "$@"
}

compose "$@"
