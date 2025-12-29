# FastAPI Login Management Application

A FastAPI application with MySQL connectivity and user authentication features.

## Features

- User Registration API
- User Login API with JWT authentication
- MySQL database integration
- Password hashing with bcrypt
- JWT token-based authentication

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Database

1. Create a `.env` file in the root directory (copy from `.env.example`):
```bash
cp .env.example .env
```

2. Update the `.env` file with your MySQL credentials:
```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=fastapi_db
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

3. Initialize the database (Python script):
```bash
python init_db.py
```

Alternatively, you can manually create the MySQL database:
```sql
CREATE DATABASE fastapi_db;
```

### 3. Run the Application

```bash
uvicorn main:app --reload
```

The application will be available at:
- API: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## API Endpoints

### Authentication Endpoints

#### Register User
- **POST** `/auth/register`
- **Request Body:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```
- **Response:** User details (without password)

#### Login
- **POST** `/auth/login`
- **Request Body:**
```json
{
  "username": "john_doe",
  "password": "securepassword123"
}
```
- **Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Get Current User
- **GET** `/auth/me`
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:** Current user details

## Project Structure

```
assignment_3/
├── main.py              # FastAPI application entry point
├── config.py            # Configuration settings
├── database.py          # Database connection and session
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic schemas for request/response
├── auth.py              # Authentication utilities
├── init_db.py           # Python script to initialize database
├── routers/
│   ├── __init__.py
│   └── auth.py          # Authentication routes
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## Security Notes

- Passwords are hashed using bcrypt
- JWT tokens are used for authentication
- Change the `SECRET_KEY` in production
- Use environment variables for sensitive data
- In production, configure CORS properly

