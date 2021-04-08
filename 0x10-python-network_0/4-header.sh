#!/bin/bash
# Script that displays all HTTP methods the server will accept.
curl -sL "$1" -X GET -d "X-HolbertonSchool-User-Id=98"
