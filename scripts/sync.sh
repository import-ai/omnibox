#!/usr/bin/env bash

for dir in "web" "backend" "wizard"; do
    (
        cd "$dir" && git fetch --all && git checkout main && git pull origin main && git submodule init && git submodule update
    ) &
done

(
    cd "client/browser-extension" && git fetch --all && git checkout main && git pull origin main && git submodule init && git submodule update
) &

wait
