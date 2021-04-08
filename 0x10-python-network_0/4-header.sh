#!/bin/bash
# Script that displays all HTTP methods the server will accept.
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id=98"
