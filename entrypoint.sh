#!/bin/bash
set -e

python backend/create_tables.py

exec python backend/server.py