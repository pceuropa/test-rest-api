#!/bin/sh

while inotifywait -r -e modify . --exclude .pytest_cache
  do
    clear
    pytest -v -p no:cacheprovider tests.py 
  done
