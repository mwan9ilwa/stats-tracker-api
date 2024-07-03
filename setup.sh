#!/bin/bash

# Create main directory structure
mkdir -p app/api app/models app/services app/utils

# Create __init__.py files
touch app/__init__.py app/api/__init__.py app/models/__init__.py app/services/__init__.py app/utils/__init__.py

# Create API route files
touch app/api/auth.py app/api/user.py app/api/repo.py

# Create service file
touch app/services/github_service.py

# Create utils file
touch app/utils/helpers.py

# Create config and run files
touch config.py run.py

# Create .env file
echo "GITHUB_CLIENT_ID=Ov23liuC83z5ni5luS0c
GITHUB_CLIENT_SECRET=922eb8fc2b360b3b052b8136773937ce30646413
GITHUB_REDIRECT_URI=http://localhost:5000/api/auth/callback" > .env

# Create .gitignore file
echo "venv/
__pycache__/
*.pyc
.env" > .gitignore

echo "Project structure created successfully!"