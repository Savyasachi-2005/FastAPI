# FastAPI

A robust, feature-rich API server built using [FastAPI](https://fastapi.tiangolo.com/) with advanced authentication, role-based access control, and hospital management capabilities.  
This repository provides a production-ready foundation for building secure, scalable RESTful APIs with Python.

---

## 🚦 What This Repository Contains

This FastAPI application provides comprehensive features for building enterprise-grade APIs with Python.  
Below is a summary of the main components and features:

### 🗂️ Main Components

- **main.py**: Entry point for the FastAPI application; configures middleware, exception handling, and includes all routers.
- **app/**: Houses application modules:
  - **routers/**: API route definitions (user, hospital, authentication)
  - **models/**: SQLAlchemy ORM models for User, Hospital, etc.
  - **middleware/**: Custom middleware components
- **repo/**: Contains the logic for user, hospital, and authentication operations.
- **schemas.py**: Pydantic models for request/response data validation and serialization.
- **db.py**: Database configuration and session management.
- **utils/**: 
  - **hashing.py**: Password hashing utilities
  - **auth.py**: Authentication utilities for JWT and OAuth2
  - **email.py**: Email verification utilities
- **exceptions.py**: Custom exception handling
- **requirements.txt**: Python dependencies.

---

## 🌟 Features

- **High Performance**: Powered by Starlette and Uvicorn for asynchronous request handling.
- **Authentication & Security**:
  - JWT-based authentication with access and refresh tokens
  - OAuth2 integration
  - Password hashing and validation
  - Email verification system
- **Role-Based Access Control**: Granular permissions management for different user types (admin, regular users).
- **Advanced Middleware**:
  - CustomASGIMiddleware for request processing
  - HeaderMiddleware for custom response headers
  - Request/response logging
- **Hospital Management**: Complete CRUD operations for hospital resources with role-based restrictions.
- **User Management**: Comprehensive user account system with email verification.
- **Exception Handling**: Custom APIException framework for consistent error responses.
- **Interactive API Docs**: Swagger UI and ReDoc built-in.
- **Type Hints**: Full support for Python type hints for better code clarity and editor assistance.
- **Scalable Architecture**: Modular design for easy extension and maintenance.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- SQL database (SQLite for development, PostgreSQL recommended for production)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Savyasachi-2005/FastAPI.git
    cd FastAPI
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory with:
    ```
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    REFRESH_TOKEN_EXPIRE_DAYS=7
    EMAIL_HOST=smtp.example.com
    EMAIL_PORT=587
    EMAIL_USERNAME=your_email@example.com
    EMAIL_PASSWORD=your_email_password
    DATABASE_URL=sqlite:///./app.db
    ```

### Running the API Server

```bash
uvicorn main:app --reload
```

- By default, the app will be running at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Interactive documentation available at:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🏗️ Project Structure

```
FastAPI/
├── main.py                # Entry point for FastAPI app
├── requirements.txt       # Python dependencies
├── app/                   # Application modules
│   ├── routers/           # API route definitions
│   │   ├── user.py
│   │   ├── hospital.py
│   │   └── auth.py
│   ├── models/            # SQLAlchemy models
│   │   ├── user.py
│   │   └── hospital.py
│   └── middleware/        # Custom middleware components
│       ├── headers.py
│       └── logging.py
├── repo/                  # Business logic implementation
├── schemas.py             # Pydantic models
├── db.py                  # Database configuration
├── utils/                 # Utility functions
│   ├── hashing.py         # Password hashing
│   ├── auth.py            # JWT token handling
│   └── email.py           # Email verification
├── exceptions.py          # Custom exception handling
└── README.md
```

---

## 🔐 Authentication Flow

The API uses a JWT-based authentication system:

1. **Registration**: Users register with email, password, and other details.
2. **Email Verification**: A verification token is sent to the user's email.
3. **Login**: After email verification, users can login to receive access and refresh tokens.
4. **Access Protected Routes**: Use the access token in the Authorization header.
5. **Token Refresh**: When the access token expires, use the refresh token to get a new one.

Example authentication header:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## 👥 User Roles and Permissions

The API implements role-based access control with the following roles:

- **Admin**: Full system access, including hospital management.
- **Doctor**: Access to patient records and limited hospital data.
- **Patient**: Access to personal records only.
- **Guest**: Limited to public endpoints.

---

## 🏥 Hospital Management

The hospital management system includes:

- Hospital registration and management
- Department organization
- Staff assignment
- Patient records
- Appointment scheduling

All operations are protected by role-based permissions.

---

## 🧑‍💻 Example Usage

- Register a new user:
  ```bash
  curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d '{"email": "user@example.com", "password": "securepassword", "name": "John Doe"}'
  ```

- Authenticate and get tokens:
  ```bash
  curl -X POST "http://127.0.0.1:8000/auth/token" -H "Content-Type: application/json" -d '{"username": "user@example.com", "password": "securepassword"}'
  ```

- Access protected endpoint:
  ```bash
  curl "http://127.0.0.1:8000/users/me" -H "Authorization: Bearer your_access_token"
  ```

- Refresh expired token:
  ```bash
  curl -X POST "http://127.0.0.1:8000/auth/refresh" -H "Content-Type: application/json" -d '{"refresh_token": "your_refresh_token"}'
  ```

- Create a hospital (admin only):
  ```bash
  curl -X POST "http://127.0.0.1:8000/hospitals/" -H "Authorization: Bearer your_access_token" -H "Content-Type: application/json" -d '{"name": "General Hospital", "address": "123 Main St", "contact_number": "555-1234"}'
  ```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/Savyasachi-2005/FastAPI/issues).

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Starlette](https://www.starlette.io/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [JWT](https://jwt.io/)

---

Happy coding! 🚀  
NOCTABYTE
