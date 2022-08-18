#!/bin/bash
#the size of the body of the response
curl -sI "$1" | grep "content-length" | cut -f2 -d:
