#!/bin/sh
find . -name *.csv | sed -e 's|^\./||g' | sort > index
