#!/usr/bin/env bash

function compose() {
    cd backend && docker compose -f base.yaml -f dev.yaml "$@" && cd ../wizard && docker compose -f compose.yaml "$@"
}

compose "$@"
