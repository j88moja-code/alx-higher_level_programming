#!/bin/bash
# send a post requst with json file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
