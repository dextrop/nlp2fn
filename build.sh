#!/bin/bash

echo "Removing Old Files"
rm -rf dist nlp2fn.egg-info

echo "Start Building"
python -m build
