#!/bin/bash
#get status codes
curl -sI -w '%{response_code}' "$1" -o /dev/null
