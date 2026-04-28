🏋️ Gym Membership API
A RESTful API for managing gym memberships, built with Django and Django REST Framework. It supports multi-gym management, role-based user access, membership tracking, and payment processing.

📁 Project Structure
gym-membership-api/
├── accounts/       # Custom user model with role-based access control
├── config/         # Project settings and URL configuration
├── gyms/           # Gym and membership management
├── payments/       # Payment model, serializers, and views
├── manage.py
└── db.sqlite3

✨ Features

Custom User Model — Role-based authentication (e.g., admin, member)
Gym Management — Create and manage multiple gym locations with ownership permissions
Membership Management — Track memberships with nested serializer support
Payment Processing — Record and retrieve payment data per membership
Permission Control — Public read access with restricted create/update/delete operations


🛠️ Tech Stack
LayerTechnologyLanguagePythonFrameworkDjangoAPIDjango REST FrameworkDatabaseSQLite (development)

🚀 Getting Started
Prerequisites

Python 3.8+
pip

Installation

Clone the repository

bash   git clone https://github.com/shaad4/gym-membership-api.git
   cd gym-membership-api

Create and activate a virtual environment

bash   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate

Install dependencies

bash   pip install -r requirements.txt

Apply migrations

bash   python manage.py migrate

Create a superuser

bash   python manage.py createsuperuser

Run the development server

bash   python manage.py runserver
The API will be available at http://127.0.0.1:8000/

📡 API Endpoints
Accounts
MethodEndpointDescriptionAuth RequiredPOST/api/accounts/register/Register a new userNoPOST/api/accounts/login/Obtain auth tokenNo
Gyms
MethodEndpointDescriptionAuth RequiredGET/api/gyms/List all gymsNoPOST/api/gyms/Create a gymYesGET/api/gyms/{id}/Retrieve a gymNoPUT/api/gyms/{id}/Update a gymYes (Owner)DELETE/api/gyms/{id}/Delete a gymYes (Owner)
Memberships
MethodEndpointDescriptionAuth RequiredGET/api/memberships/List all membershipsNoPOST/api/memberships/Create a membershipYesGET/api/memberships/{id}/Retrieve a membershipNoPUT/api/memberships/{id}/Update a membershipYes (Owner)DELETE/api/memberships/{id}/Delete a membershipYes (Owner)
Payments
MethodEndpointDescriptionAuth RequiredGET/api/payments/List all paymentsYesPOST/api/payments/Record a paymentYesGET/api/payments/{id}/Retrieve a paymentYes

🔐 Authentication
This API uses Token-based authentication. Include the token in the request header:
Authorization: Token <your_token_here>

🗂️ Environment Configuration
Update config/settings.py for production use:

Set DEBUG = False
Configure ALLOWED_HOSTS
Replace SQLite with a production database (e.g., PostgreSQL)
Set a secure SECRET_KEY via environment variables


🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add your feature')
Push to the branch (git push origin feature/your-feature)
Open a Pull Request


📄 License
This project is open source and available under the MIT License.

👤 Author
Mohammed Shaad N — @shaad4
