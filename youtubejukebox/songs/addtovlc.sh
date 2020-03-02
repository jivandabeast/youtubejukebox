#!/bin/bash

fileName=$(find . -type f -name "*$1*" | cut -c 3-)

echo "$fileName"

cvlc "$fileName"
