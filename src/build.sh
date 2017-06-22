#!/bin/bash
transcrypt -b -m -e 6 -n main.py
browserify -o ../build.js __javascript__/main.js
