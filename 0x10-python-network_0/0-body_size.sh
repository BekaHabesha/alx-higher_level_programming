#!/bin/bash
# sends a request and Displays the byte size of
# the HTTP response header for a given URL.
# Author Bereket Dereje
curl -s "$1" | wc -c
