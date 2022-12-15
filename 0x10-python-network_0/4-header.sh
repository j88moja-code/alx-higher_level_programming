#!/bin/bash
# send a get request with custom data and display body
curl -s "$1" -X GET -H 'X-School-User-Id: 98'
