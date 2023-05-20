#!/bin/bash

pip install --upgrade pip setuptools wheel
pip install tqdm
pip install --user --upgrade twine
python -m pip install --upgrade build

echo "\n\n\nSystem variable set, running build\n\n\n"
./build.sh