#!/bin/bash
/entrypoint/wait_for_it.sh kafka:9092 -- python3 -u app.py
