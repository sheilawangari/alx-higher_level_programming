#!/bin/bash
# Put the cotent legnt
curl -sI "$1" | grep Content-Length | cut -d " " -f2-

