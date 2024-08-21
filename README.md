# Task Management Application

This is a simple Task Management application built using Django. It allows users to create, update, delete, and manage tasks. The application features user authentication, task categorization, and the ability to mark tasks as completed.

## Features

- User authentication (sign up, login, logout)
- Create, update, and delete tasks
- Mark tasks as completed
- Categorize tasks by priority or tags
- Responsive design for mobile and desktop views

## Requirements

- Python 3.11 or above
- Django 4.x or above
- crispy-bootstrap5 (for form styling)
- SQLite (default) or PostgreSQL for production

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/<your-username>/Task-Management-Using-Django.git
    cd Task-Management-Using-Django
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Configuration

### Database

The application uses SQLite by default. If you want to use PostgreSQL or another database, update the `DATABASES` setting in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
