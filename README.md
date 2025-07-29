# FastAPI

A fast and efficient web API server built using [FastAPI](https://fastapi.tiangolo.com/).  
This repository serves as a starter template and learning project for building scalable, production-ready RESTful APIs with Python.

---

## 🚦 What This Repository Contains

This FastAPI starter template provides everything you need to build scalable, production-ready RESTful APIs with Python.  
Below is a summary of the main components and features provided:

### 🗂️ Main Components

- **main.py**: Entry point for the FastAPI application; sets up the app and includes routers for blog, user, and login functionalities.
- **app/**: Houses application modules:
  - **routers/**: API route definitions (e.g., `blog.py`, `user.py`, `login.py`)
  - **models/**: SQLAlchemy ORM models for `User` and `Blog`
- **repo/**: Contains the logic for blog and user operations (CRUD functionality).
- **schemas.py**: Pydantic models for request/response data validation and serialization.
- **db.py**: Database configuration and session creation.
- **hashing.py**: Password hashing utilities (bcrypt).
- **requirements.txt**: Python dependencies.
- **README.md**: Setup instructions, usage, features, and project structure.

---

## 🌟 Features

- **High performance**: Powered by Starlette and Uvicorn for asynchronous request handling.
- **Automatic validation**: Data validation using Pydantic models.
- **Interactive API docs**: Swagger UI and ReDoc built-in.
- **Type hints**: Full support for Python type hints for better code clarity and editor assistance.
- **Extensible**: Easily add authentication, database, and more.
- **User Management**: Create, fetch, and manage users with password hashing and validation.
- **Blog CRUD**: Create, read, update, and delete blog posts, linked to users.
- **Authentication Structure**: Foundation to add authentication (token-based, etc.).
- **Scalable Structure**: Modular design so you can easily add more routers, models, and services.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Savyasachi-2005/FastAPI.git
    cd FastAPI
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
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
├── main.py              # Entry point for FastAPI app
├── requirements.txt     # Python dependencies
├── app/                 # Application modules (routers, models, services, etc.)
│   ├── routers/
│   ├── models/
│   └── ...
├── repo/                # Implementation logic for blog and user operations
├── schemas.py           # Pydantic models for serialization & validation
├── db.py                # Database config and session management
├── hashing.py           # Password hashing utilities
└── README.md
```

---

## 🧑‍💻 Example Usage

- Make a GET request:
    ```bash
    curl http://127.0.0.1:8000/
    ```
- Explore the interactive docs at `/docs` for more endpoints.
- Use the endpoints for user and blog CRUD operations:
    - See `/users` and `/blogs` routes in the interactive docs.

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

---

Happy coding! 🚀  
NOCTABYTE
