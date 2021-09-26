#! /usr/bin/env bash

# Let the DB start
python /app/app/be_prestart.py

# Create initial data in DB
python /app/app/initial_data.py
