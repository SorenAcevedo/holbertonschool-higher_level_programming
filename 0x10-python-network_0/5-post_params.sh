#!/bin/bash
# Script that displays all HTTP methods the server will accept.
curl "$1" -X POST -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD"
