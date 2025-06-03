#!/usr/bin/env bash
for dir in "web" "backend" "wizard"; do
    cd "$dir" && git checkout main && git pull origin main
    cd ..
done

cd "client/browser-extension" && git checkout main && git pull origin main
cd "../.."
