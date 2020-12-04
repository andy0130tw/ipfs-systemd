#!/bin/bash

mkdir -p dist/

[ -z $(which nuitka) ] && { echo "nuitka is required but cannot be found on PATH."; exit 1; }

TARGET=dist/ipfsi
python3 $(which nuitka) ./ipfsi.py -o $TARGET
sudo chown root:root $TARGET
sudo chmod u+s $TARGET
