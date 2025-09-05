#!/bin/bash
cd /root/luxlab-clean/luxlab-omnisystem
source venv/bin/activate
gunicorn -w 4 -b 127.0.0.1:8080 --timeout 120 app:app --daemon --log-file logs/gunicorn.log
