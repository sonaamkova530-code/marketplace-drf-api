# 🛒 Marketplace drf API

A robust, fully containerized RESTful API for an e-commerce marketplace platform built with Django and Django REST Framework (DRF).

### 🛠️ Tech Stack & Features
* **Backend Framework:** Django 6.0+ & Django REST Framework (DRF)
* **Database:** PostgreSQL 15
* **Authentication:** JWT (JSON Web Tokens) via `djangorestframework_simplejwt`
* **API Documentation:** OpenAPI 3.0 & Interactive Swagger UI via `drf-spectacular`
* **Containerization:** Docker & Docker Compose
* **Media Handling:** Image processing for products/profiles via `Pillow`

---

## ⚙️ Configuration & Environment Variables

Before running the application, you need to configure the environment variables. Create a `.env` file in the root directory of the project and populate it with the following template:

```env
# Django Settings
SECRET_KEY=your_secure_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL Database Settings
DB_NAME=marketplace_db
DB_USER=postgres_user
DB_PASSWORD=postgres_secure_password
DB_HOST=db
DB_PORT=5432 
```

## 🚀 Getting Started

Follow these steps to get the project up and running locally using Docker.

### 1. Prerequisites
Make sure you have the following installed on your system:
* **Docker** & **Docker Compose**
* **WSL2** (if you are running on Windows)

### 2. Setup Environment Variables
Clone the repository and create a `.env` file in the root directory as explained in the Configuration section above.

### 3. Build and Run the Containers
Run the following command to build the Docker images and start all services (database and API):

```bash
docker compose up --build
```
*Note: Database migrations will run automatically on startup thanks to the automated container command.*


### 4. Create a Superuser (Admin Access)
To access the Django Admin panel, you need to create an administrative account. Open a new terminal tab and run:

```bash
docker compose exec api python manage.py createsuperuser