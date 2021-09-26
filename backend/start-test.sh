#! /usr/bin/env bash

# Start Testing
docker-compose -f docker-compose.testing.yml up --build --remove-orphans
