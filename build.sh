#!/bin/bash

mkdir -p dist/

TARGET=dist/ipfsi
python3 /usr/bin/nuitka ./ipfsi.py -o $TARGET
sudo chown root:root $TARGET
sudo chmod u+s $TARGET
