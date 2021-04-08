#!/bin/bash
# Script that makes a Http request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f2 