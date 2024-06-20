#!/bin/bash

# Navigate to the application directory
cd /path/to/skincheckapp || { echo "Failed to navigate to skincheckapp directory"; exit 1; }

# Activate the virtual environment
source venv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }

# Set environment variables
export FLASK_APP=main.py
export GOOGLE_APPLICATION_CREDENTIALS=keys/key.json
export UPLOAD_FOLDER=./uploads

# Start Gunicorn with nohup and redirect output to a log file
nohup gunicorn -b 0.0.0.0:8080 -w 4 --access-logfile - main:app > gunicorn.log 2>&1 &

# Output the PID of the Gunicorn process
echo "Gunicorn started with PID $!"

