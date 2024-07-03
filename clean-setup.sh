#!/bin/bash

# Create and activate a new virtual environment
python3 -m venv venv
source venv/bin/activate

# Install only the necessary packages
pip install Flask==3.0.3 Flask-Cors==4.0.1 python-dotenv==1.0.1 requests==2.25.1

# Generate a clean requirements.txt
pip freeze > requirements.txt

echo "Clean environment set up with only necessary dependencies."
echo "New requirements.txt file generated."