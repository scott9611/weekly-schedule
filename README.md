# Django REST API with JWT Authentication

This project demonstrates how to implement JSON Web Token (JWT) authentication in a Django REST Framework API using the `djangorestframework-simplejwt` library.

## Features

- Django REST Framework API
- JWT Authentication
- Token refresh functionality

## Requirements

- Python 3.8+
- Django 3.2+
- Django REST Framework 3.12+
- djangorestframework-simplejwt 4.6+

## Installation

### Local Development

1. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install the required packages (Ensure you have poetry installed):
   ```
   poetry install
   ```

3. Apply migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   (username: admin, email: admin@example.com, password: 12345)
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

### Docker Development

1. Setup Docker on your machine

2. Run the Docker container:
   ```
   docker compose -f docker-compose.dev.yml up -d --build
   ```


## JWT Authentication

This project uses `djangorestframework-simplejwt` for JWT authentication. Here's how to use it:

1. Obtain a token pair (access and refresh tokens):
   ```
   POST /api/token/
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. Use the access token in the Authorization
```
   Authorization: Bearer <your_access_token>
   ```

3. Refresh the access token using the refresh token:
   ```
   POST /api/token/refresh/
   {
     "refresh": "<your_refresh_token>"
   }
   ```

## API Endpoints

- `/api/token/`: Obtain a token pair
- `/api/token/refresh/`: Refresh access token
- `/protected/`: A protected view (requires authentication)

## Configuration

JWT settings can be configured in `settings.py`:

- `SIMPLE_JWT`: Customize token settings

## Testing

To run the tests:
```
python manage.py test
``` 
