#!/bin/bash
#send header variables
curl -sL "$1" -X GET -H "X-School-User-Id: 98"
