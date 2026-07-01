# 🏥 Hospital Management System

A scalable and professional Hospital & Clinic Management System built with **Django** and **PostgreSQL**.

This project is designed to simulate a real-world healthcare management platform while following clean architecture and scalable software engineering principles.

---

# 🚀 About The Project

The goal of this project is to build a complete healthcare management system that can be used in hospitals and clinics.

The project focuses on:

- Clean Architecture
- Scalable Database Design
- Role-Based Access Control (RBAC)
- REST API Development
- AI-assisted Healthcare Features (Upcoming)

---

# ✨ Current Features

## Authentication & User Management

- ✅ Custom User Model
- ✅ Environment Variables (.env)
- ✅ PostgreSQL Integration
- ✅ Role-Based Access Control

Supported Roles:

- Manager
- Doctor
- Nurse
- Receptionist
- Patient

---

## Doctor Management

- ✅ Doctor Profile
- ✅ Medical License Number
- ✅ Medical Specialization
- ✅ Django Admin Customization

Supported Specializations include:

- General Practitioner (GP)
- Dentist
- Orthopedic
- Cardiology
- Dermatology
- Neurology
- Pediatrics
- Gynecology
- Ophthalmology
- ENT
- Psychiatry

---

## Nurse Management

- ✅ Nurse Profile
- ✅ Phone Number
- ✅ Django Admin Customization

---

## Patient Management

- ✅ Patient Profile
- ✅ Date of Birth
- ✅ Gender
- ✅ Blood Group
- ✅ Emergency Contact
- ✅ Underlying Disease Information
- ✅ Patient Priority Level (Triage Ready)

Priority Levels:

- Low
- Medium
- High
- Emergency

---

## Shift Management

- ✅ Shift Model
- ✅ Doctor Shift
- ✅ Nurse Shift
- ✅ Department-based Shifts
- ✅ Shift Status
- ✅ Shift Start Time
- ✅ Shift End Time

---

## Medical Services

- ✅ Service Management
- ✅ Service Duration
- ✅ Service Description
- ✅ Service Categorized by Medical Specialization

---

## Django Admin

Customized Admin Panels for:

- Users
- Doctors
- Nurses
- Patients
- Receptionists
- Shifts
- Services

---

# 🚧 Upcoming Features

## Appointment System

- Appointment Booking
- Smart Scheduling
- Conflict Detection
- Doctor Availability

---

## Medical Records

- Patient Medical History
- Diagnosis
- Treatment Plan
- Visit History

---

## Prescription System

- Medication
- Dosage
- Duration
- Notes

---

## AI Features (Planned)

- 🤖 AI Symptom Analyzer
- 🤖 Medical Specialization Recommendation
- 🤖 Smart Appointment Recommendation
- 🤖 Intelligent Patient Triage Assistance

---

## Notifications

- Shift Reminder
- Appointment Reminder
- Email Notifications
- SMS Notifications

---

## Dashboard

- Hospital Statistics
- Doctor Analytics
- Patient Analytics
- Appointment Reports

---

# 🛠 Tech Stack

Backend

- Python
- Django
- Django REST Framework

Database

- PostgreSQL

Authentication

- JWT Authentication

Documentation

- Swagger / OpenAPI

Background Tasks *(Planned)*

- Celery
- Redis

Deployment *(Planned)*

- Docker

---

# 📂 Project Structure

```
hospital-management-system/

accounts/
hospital/

config/

manage.py
requirements.txt
README.md
```

---

# ⚙️ Installation

Clone repository

```bash
git clone https://github.com/Kian-kianmehr/hospital-management-system.git
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

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

---

# 🔐 Environment Variables

Create a `.env` file:

```env
DB_NAME=hospital_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY=your_secret_key
DEBUG=True
```

---

# ▶️ Run Project

Apply migrations

```bash
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

Run development server

```bash
python manage.py runserver
```

---

# 🗺 Roadmap

- ✅ Authentication System
- ✅ Role Management
- ✅ Doctor Management
- ✅ Nurse Management
- ✅ Patient Management
- ✅ Shift Management
- ✅ Medical Services

### Next Milestones

- 🔜 Appointment System
- 🔜 Medical Records
- 🔜 Prescription System
- 🔜 AI Assistant
- 🔜 REST API
- 🔜 Docker Deployment

---

# 👨‍💻 Author

**Kian Kianmehr**

Backend Developer | Python & Django Developer

GitHub:

https://github.com/Kian-kianmehr

---

# ⭐ Project Status

🚧 **Currently under active development**

The project is continuously being improved with new healthcare modules and AI-powered features.