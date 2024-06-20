#!/bin/bash

python3 -m venv venv
source venv/bin/activate

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

echo "Dependencies has been installed succesfuly"