#!/bin/bash
#get status codes
curl -sI $1| grep HTTP/1.1|cut -d ' ' -f2
