#!/bin/bash
# Drop the database (depends on your DB backend)
# For SQLite just delete the db file
rm db.sqlite3

# For Postgres/MySQL, drop and recreate the schema manually

# Delete old migration files (optional but cleaner)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Recreate migrations
python manage.py makemigrations

# Apply them fresh
python manage.py migrate
