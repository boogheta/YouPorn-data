#!/bin/bash

if ! test -s YouPorn-Embed-Videos-Dump.csv; then
  wget "http://www.youporn.com/YouPorn-Embed-Videos-Dump.zip" -O YouPorn-Embed-Videos-Dump.zip
  unzip YouPorn-Embed-Videos-Dump.zip
fi

cat YouPorn-Embed-Videos-Dump.csv | sed 's/|[^|]*|[^|]*$//' | sed 's/^.*|"\?\([^|]*\)$/\1/' | sed 's/"$//' | grep . > tags-youporn.csv

./prepare_network.py tags-youporn.csv


