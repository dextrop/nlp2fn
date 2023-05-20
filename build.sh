#!/bin/bash

echo "Removing Old Files"
rm -rf build dist ask_jennie.egg-info

echo "Start Building"
python -m build
