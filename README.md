# Hospital Management System 🏥

A professional hospital management system built with Django and PostgreSQL.

## About The Project

This project is a backend system for managing hospital operations.

The goal is to build a scalable system including:

* User management
* Role-based access control
* Doctors management
* Patients management
* Appointments
* Medical records
* Prescriptions

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Redis
* Celery
* Docker
* JWT Authentication
* Swagger API Documentation

## Current Features

✅ PostgreSQL database integration
✅ Environment variables configuration
✅ Custom User Model
✅ Role system:

* Admin
* Doctor
* Nurse
* Reception
* Patient

✅ Django Admin customization

## Setup

Clone the repository:

```bash
git clone https://github.com/Kian-kianmehr/hospital-management-system.git
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
DB_NAME=hospital_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Run migrations:

```bash
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

Run server:

```bash
python manage.py runserver
```

## Development Status

🚧 Currently under active development.

## Author

Kian Kianmehr
