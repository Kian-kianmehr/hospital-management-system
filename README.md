# 🏥 Hospital Management System

A scalable and production-oriented Hospital Management System built with **Django** and **PostgreSQL**.

The goal of this project is to simulate real-world hospital workflows while following clean architecture and backend best practices.

---

# ✨ Features

## Authentication & User Management

* Custom User Model
* Role-Based Access Control
* Admin
* Doctor
* Nurse
* Receptionist
* Patient

---

## Doctor Management

* Doctor Profiles
* Doctor Types

  * General Practitioner (GP)
  * Specialist
* Medical License Number
* Medical Specialization

---

## Patient Management

* Patient Profiles
* Blood Group
* Emergency Contact
* Medical Information

---

## Hospital Workflow

Patients follow a real hospital workflow:

```
Registration

↓

Patient Profile

↓

Describe Medical Problem

↓

Reception Review

↓

Choose Required Specialization

↓

Appointment Booking

↓

Doctor Visit

↓

Prescription / Referral / Procedure

↓

Follow-up Appointment (if required)
```

The system is designed to reflect how clinics and hospitals commonly operate.

---

# 🚧 Planned Features

* Reception Dashboard
* Appointment Management
* Doctor Shift Management
* Visit Reports
* Medical Prescriptions
* Patient Referrals
* Medical Procedures
* Notification System
* Email Reminders
* REST API
* JWT Authentication
* Swagger Documentation
* Docker Deployment
* Redis
* Celery Background Tasks

---

# 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Redis
* Celery
* Docker
* JWT
* Swagger / OpenAPI

---

# 📂 Project Structure

```
hospital-management/

├── accounts/
│   ├── models.py
│   ├── admin.py
│   └── ...
│
├── hospital/
│   ├── models.py
│   ├── admin.py
│   └── ...
│
├── config/
│
├── manage.py
│
└── requirements.txt
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Kian-kianmehr/hospital-management-system.git
```

Move into the project

```bash
cd hospital-management-system
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
DB_NAME=hospital_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin account

```bash
python manage.py createsuperuser
```

Run the server

```bash
python manage.py runserver
```

---

# 📈 Development Status

Current Progress

* ✅ PostgreSQL Configuration
* ✅ Environment Variables
* ✅ Custom User Model
* ✅ Role System
* ✅ Django Admin Customization
* ✅ Doctor Profiles
* ✅ Patient Profiles
* ✅ Medical Specializations
* 🚧 Hospital Workflow
* 🚧 Appointment System
* 🚧 Shift Management
* 🚧 REST API

---

# 🎯 Project Goal

This project focuses on building a maintainable backend architecture for hospital management.

Instead of trying to replace medical professionals, the system models the real operational workflow inside a healthcare organization, including patient registration, reception review, appointment scheduling, doctor visits, referrals, prescriptions, and follow-up care.

---

# 👨‍💻 Author

**Kian Kianmehr**
