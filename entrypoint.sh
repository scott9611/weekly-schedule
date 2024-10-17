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

# Create superuser
echo "Creating superuser"
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '12345') if not User.objects.filter(username='admin').exists() else print('Superuser already exists.')"

# Ensure Nginx can access static files
chmod -R 755 /app/staticfiles

# Start server
exec "$@"