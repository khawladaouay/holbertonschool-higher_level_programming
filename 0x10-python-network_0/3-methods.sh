#!/bin/bash
# Bash script that takes in a URL and displays all HTTP method
curl -sI "$1" | grep "Allow" | cut -f2- -d " "
