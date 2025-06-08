#!/usr/bin/env bash

function compose() {
    cd backend && docker compose -f base.yaml -f build.yaml "$@" && cd ../wizard && docker compose -f compose.yaml "$@"
}

compose "$@"
