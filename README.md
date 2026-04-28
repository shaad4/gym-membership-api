# 🏋️ Gym Membership API

A RESTful API for managing gym memberships, built with **Django** and **Django REST Framework**. It supports multi-gym management, role-based user access, membership tracking, and payment processing.

---

## 📁 Project Structure

```
gym-membership-api/
├── accounts/       # Custom user model with role-based access control
├── config/         # Project settings and URL configuration
├── gyms/           # Gym and membership management
├── payments/       # Payment model, serializers, and views
├── manage.py
└── db.sqlite3
```

---

## ✨ Features

- **Custom User Model** — Role-based authentication (e.g., admin, member)
- **Gym Management** — Create and manage multiple gym locations with ownership permissions
- **Membership Management** — Track memberships with nested serializer support
- **Payment Processing** — Record and retrieve payment data per membership
- **Permission Control** — Public read access with restricted create/update/delete operations

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python |
| Framework | Django |
| API | Django REST Framework |
| Database | SQLite (development) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/shaad4/gym-membership-api.git
   cd gym-membership-api
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/`

---

## 📡 API Endpoints

### Accounts

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/accounts/register/` | Register a new user | No |
| POST | `/api/accounts/login/` | Obtain auth token | No |

### Gyms

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/gyms/` | List all gyms | No |
| POST | `/api/gyms/` | Create a gym | Yes |
| GET | `/api/gyms/{id}/` | Retrieve a gym | No |
| PUT | `/api/gyms/{id}/` | Update a gym | Yes (Owner) |
| DELETE | `/api/gyms/{id}/` | Delete a gym | Yes (Owner) |

### Memberships

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/memberships/` | List all memberships | No |
| POST | `/api/memberships/` | Create a membership | Yes |
| GET | `/api/memberships/{id}/` | Retrieve a membership | No |
| PUT | `/api/memberships/{id}/` | Update a membership | Yes (Owner) |
| DELETE | `/api/memberships/{id}/` | Delete a membership | Yes (Owner) |

### Payments

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/payments/` | List all payments | Yes |
| POST | `/api/payments/` | Record a payment | Yes |
| GET | `/api/payments/{id}/` | Retrieve a payment | Yes |

---

## 🔐 Authentication

This API uses **Token-based authentication**. Include the token in the request header:

```
Authorization: Token <your_token_here>
```

---

## 🗂️ Environment Configuration

Update `config/settings.py` for production use:

- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Replace SQLite with a production database (e.g., PostgreSQL)
- Set a secure `SECRET_KEY` via environment variables

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Mohammed Shaad N** — [@shaad4](https://github.com/shaad4)
