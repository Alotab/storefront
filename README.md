# Django E-Commerce API with JWT Authentication, Celery, and Redis
This is a Django-based eCommerce API built on top of the Django Rest Framework (DRF). The project includes user management, JWT authentication using Djoser, background task processing with Celery, and Redis as the cache and message broker. The API is designed to handle the typical operations of an e-commerce platform, including product management, order handling, and more.

## Features
* User registration, login, and JWT authentication with Djoser and JWT tokens.
* Permissions and custom permissions on specific API endpoints, models, and users.
* Background tasks management using Celery with Redis as the message broker.
* Cache management with Redis for improved performance.
* RESTful API using Django Rest Framework for eCommerce functionalities.

## Setup and Configuration
1. Clone the repository:
   ```
   git clone https://github.com/Alotab/storefront.git
   cd storefront
   ```
2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create .env file for sensitive settings (such as secret keys, database credentials, etc.):
   ```
   SECRET_KEY = ''
   DATABASE_ENGINE = ''
   DATABASE_USER = ''
   DATABASE_NAME = ''
   DATABASE_PORT = ''
   DATABASE_HOST = ''
   DATABASE_PASSWORD = ''
   ```
5. Run the migrations:
   ```
   python manage.py migrate
   ```

## Running the Application
### Starting the Django Server
To run the Django development server:
```
python manage.py runserver
```
This will start the server at http://127.0.0.1:8000/.

### Running Celery
To start the Celery worker:
```
celery -A storefront --loglevel=info
```

To start Celery beat (for periodic tasks):
```
celery -A storefront beat --loglevel=info
```





