#!/bin/bash

# Start PostgreSQL
service postgresql start

# Wait for PostgreSQL to be ready
while ! nc -z localhost 5432; do
  sleep 0.1
done

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Ensure Nginx can access static files
chmod -R 755 /app/staticfiles

# Start server
exec "$@"
