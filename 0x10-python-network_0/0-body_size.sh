#!/usr/bin/env bash
# Script that makes a Http request
# and displays the size of the body
curl -sI "$1" | grep 'Content-Length:' | cut -d ' ' -f2 