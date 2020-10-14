#!/bin/bash
/entrypoint/wait_for_it.sh kafka:9092 -- "$@"
