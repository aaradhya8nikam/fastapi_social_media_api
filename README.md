# Social Platform REST API

A RESTful backend for a social media platform, built with **FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication**. The project demonstrates backend API development, relational database design, authentication, database migrations, request validation, and API testing.

<p align="center">
  <img src="https://img.shields.io/badge/Python-Backend-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Alembic-Migrations-6BA81E" alt="Alembic">
  <img src="https://img.shields.io/badge/JWT-Authentication-black?logo=jsonwebtokens" alt="JWT">
</p>

**Repository:** [aaradhya8nikam/fastapi_social_media_api](https://github.com/aaradhya8nikam/fastapi_social_media_api)

---

## Overview

Social Platform REST API is a backend application designed to support the core functionality of a social media platform. It provides a foundation for user management, post management, and authenticated interactions through REST endpoints.

The project focuses on building a maintainable backend using modular route handlers, relational database models, schema validation, and token-based authentication.

Rather than relying on a single monolithic application file, the backend separates its responsibilities into modules for database connectivity, data models, validation schemas, authentication, and API routes.

## Features

* **User management:** Register users and retrieve user information.
* **Post management:** Create, retrieve, update, and delete posts.
* **JWT authentication:** Authenticate users and issue bearer tokens for protected operations.
* **Password security:** Hash passwords before storing them in the database.
* **Authorization:** Check post ownership before allowing protected modifications.
* **Relational database:** Persist users, posts, and associated interactions in PostgreSQL.
* **ORM-based data access:** Use SQLAlchemy to define models and interact with the database.
* **Request validation:** Use Pydantic schemas to validate incoming data and structure responses.
* **Database migrations:** Use Alembic to manage schema changes.
* **API exploration:** Inspect endpoints and schemas through FastAPI's interactive documentation.
* **API testing workflow:** Explore and validate requests using Postman and automated testing tools.

*Feature availability depends on the current implementation. Consult the live API documentation after starting the application.*

## Tech Stack

| Technology         | Purpose                         |
| ------------------ | ------------------------------- |
| Python             | Backend programming language    |
| FastAPI            | REST API framework              |
| PostgreSQL         | Relational data storage         |
| SQLAlchemy         | ORM and database interaction    |
| Pydantic           | Request and response validation |
| Alembic            | Database schema migrations      |
| JWT                | Token-based authentication      |
| Passlib / bcrypt   | Password hashing                |
| Uvicorn            | ASGI application server         |
| Pytest             | Automated testing               |
| FastAPI TestClient | API endpoint testing            |
| Postman            | Manual API testing              |

## Architecture

The application follows a modular backend architecture in which different components handle specific responsibilities.

```text
Client / API Consumer
         |
         v
    FastAPI App
         |
         v
     API Routers
    /    |     \
 Users  Posts  Authentication
    \    |     /
         v
   Dependencies
         |
         v
  SQLAlchemy ORM
         |
         v
     PostgreSQL
```

### Request lifecycle

1. A client sends an HTTP request to an API endpoint.
2. FastAPI validates the request using the relevant schema.
3. Dependencies provide the database session and authenticated user when required.
4. SQLAlchemy performs the database operation.
5. The application returns a structured response or an HTTP error.

This separation makes the code easier to understand, test, and extend.

## Project Structure

The following represents the intended module organization; adjust the tree if your current repository differs.

```text
fastapi_social_media_api/
├── app/
│   ├── main.py              # Application initialization
│   ├── config.py            # Environment-based configuration
│   ├── database.py          # Database engine and sessions
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── oauth2.py            # JWT and authentication helpers
│   ├── utils.py             # Password hashing utilities
│   └── routers/
│       ├── auth.py          # Authentication endpoints
│       ├── user.py          # User endpoints
│       ├── post.py          # Post endpoints
│       └── vote.py          # Voting or interaction endpoint
├── alembic/
│   ├── env.py               # Migration configuration
│   └── versions/            # Migration scripts
├── .postman/                # Postman-related resources, if present
├── .vscode/                 # Editor configuration
├── alembic.ini              # Alembic settings
├── requirements.txt         # Python dependencies
└── README.md
```

## Database Design

The data layer uses SQLAlchemy models to represent entities and their relationships.

### User

Stores account information, including:

* Unique email address
* Hashed password
* Creation timestamp
* Optional profile information, where implemented

### Post

Represents content created by a user. A post can include fields such as:

* Title
* Content
* Publication status
* Creation timestamp
* Owner reference

### Vote / Interaction

Represents a relationship between a user and a post, where supported by the current schema. A composite key or database constraint can prevent duplicate interactions of the same type.

Conceptually:

```text
User 1 -------- N Post

User N -------- N Post
         through Vote
```

The relational design helps maintain data consistency and associate each post with its creator.

## Authentication and Authorization

The API uses JSON Web Tokens (JWT) for token-based authentication.

### Authentication flow

1. A user registers with account credentials.
2. The password is hashed before persistence.
3. The user submits login credentials.
4. The server verifies the credentials.
5. A valid login returns a JWT access token.
6. The client includes the token in subsequent protected requests.
7. The server validates the token and identifies the current user.

Protected requests use the standard bearer-token header:

```http
Authorization: Bearer <access_token>
```

### Password security

Passwords should never be stored or returned in plain text. The application uses password-hashing utilities to verify credentials during authentication.

### Authorization

Authentication establishes who is making a request. Authorization determines what that user is allowed to do.

For example, a post owner should be able to modify their own post, while another authenticated user should not be able to modify it without permission.

## Getting Started

### Prerequisites

Install the following:

* Python 3.10 or newer, compatible with your dependencies
* PostgreSQL
* Git
* A terminal such as PowerShell or Bash

### 1. Clone the repository

```bash
git clone https://github.com/aaradhya8nikam/fastapi_social_media_api.git

cd fastapi_social_media_api
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and configure the database and authentication settings.

```dotenv
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=your_database_name
DATABASE_USERNAME=your_database_username
DATABASE_PASSWORD=your_database_password

SECRET_KEY=your_generated_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Use the exact environment-variable names expected by `app/config.py`. The example above is a template; verify that the application reads each setting before running it.

**Security:** Do not commit `.env` files or real credentials to GitHub. If a real database password has already been published, rotate it immediately.

Generate a random secret locally with Python:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Create the PostgreSQL database

Create the database and configure a user with the appropriate permissions.

For example, from a PostgreSQL administration session:

```sql
CREATE DATABASE social_platform;
```

Update the database name and credentials in your environment configuration accordingly.

### 6. Apply database migrations

After configuring the database, run:

```bash
alembic upgrade head
```

This applies the available migration revisions. If the repository does not yet contain an initial migration, create and review one before expecting the command to initialize the schema.

### 7. Start the application

From the project root:

```bash
uvicorn app.main:app --reload
```

The development server should be available at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI generates interactive documentation from the application's registered routes and schemas.

| Resource      | URL                         |
| ------------- | --------------------------- |
| Swagger UI    | http://127.0.0.1:8000/docs  |
| ReDoc         | http://127.0.0.1:8000/redoc |
| Root endpoint | `GET /`                     |

Use Swagger UI to inspect request bodies, try endpoints, and review their response schemas. Only routes registered with the main application will appear.

## API Endpoint Reference

The table below describes the intended endpoint groups. Confirm the exact paths and methods against the current source and `/docs`.

| Method   | Endpoint      | Description                                   |
| -------- | ------------- | --------------------------------------------- |
| `GET`    | `/`           | Return a basic API response                   |
| `POST`   | `/users/`     | Register a user                               |
| `GET`    | `/users/{id}` | Retrieve a user                               |
| `POST`   | `/login`      | Authenticate and obtain an access token       |
| `GET`    | `/posts/`     | Retrieve posts                                |
| `POST`   | `/posts/`     | Create a post                                 |
| `GET`    | `/posts/{id}` | Retrieve a post                               |
| `PUT`    | `/posts/{id}` | Update a post                                 |
| `DELETE` | `/posts/{id}` | Delete a post                                 |
| `POST`   | `/vote/`      | Create or modify a supported vote interaction |

The endpoint table is an intended API reference, not a claim that every listed route has been verified to work.

## Example Requests

### Register a user

`POST /users/`

```json
{
  "email": "developer@example.com",
  "password": "replace-with-a-strong-password"
}
```

### Authenticate a user

`POST /login`

When using FastAPI's `OAuth2PasswordRequestForm`, submit form data rather than JSON:

```text
username=developer@example.com
password=replace-with-your-password
```

The username field is commonly matched against the registered email address.

A successful login is expected to return a response similar to:

```json
{
  "access_token": "<access-token>",
  "token_type": "bearer"
}
```

### Create a post

`POST /posts/`

Include a valid bearer token and submit a JSON body matching the application's post-creation schema.

```json
{
  "title": "My first post",
  "content": "Building and learning with FastAPI.",
  "published": true
}
```

### Access a protected endpoint

```http
Authorization: Bearer <access-token>
```

The exact request fields and response structure should match the Pydantic schemas exposed in Swagger UI.

## Database Migrations with Alembic

Alembic manages database schema changes as the application evolves.

```bash
# Inspect the current database revision
alembic current

# View migration history
alembic history

# Apply all available migrations
alembic upgrade head

# Generate a migration after changing models
alembic revision --autogenerate -m "describe schema change"
```

Always review autogenerated migration scripts before applying them. Autogeneration may not capture every intended change or data migration.

## Testing

The project uses a backend testing workflow involving Pytest, FastAPI TestClient, and Postman.

Recommended test cases include:

* User registration with valid and invalid inputs
* Duplicate email registration
* Successful and unsuccessful login attempts
* Missing, invalid, and expired access tokens
* Creating and retrieving posts
* Updating or deleting posts owned by the current user
* Attempts to modify another user's posts
* Database validation and error handling
* Voting behavior and duplicate interactions, if implemented

Run the configured test suite with:

```bash
pytest
```

The command assumes that tests and their dependencies are configured in the repository. No test-pass claim is made here; run the suite and verify its results before reporting test coverage.

## Engineering Considerations

### Configuration and secrets

Database connection details and JWT signing keys should come from environment-based configuration. Avoid hardcoded credentials and ensure `.env` is ignored by Git.

### Database sessions

Use a consistent SQLAlchemy session dependency across route handlers. Sessions should be properly closed, and database exceptions should be handled without exposing internal credentials or implementation details.

### API validation

Use Pydantic schemas to validate input and define the data returned to clients. Public response schemas should never expose password hashes.

### Authorization

Enforce ownership checks on every protected state-changing operation. Do not rely only on the client to restrict access.

### Testing and reliability

Automated tests should cover successful requests, expected failures, authorization boundaries, and database behavior.

## Known Items to Verify

Before treating the repository as a fully functional or production-ready backend, review the following items in the current source:

* Ensure database connectivity uses the configured environment variables consistently rather than a separate hardcoded connection.
* Ensure the JWT creation function has the same name in its definition and every import/call site.
* Confirm that all intended routers, including the vote router if applicable, are registered in `app/main.py`.
* Check for duplicate route declarations, particularly multiple handlers using `GET /posts/`.
* Verify SQLAlchemy query syntax in post retrieval and deletion handlers.
* Ensure post response schemas match the objects returned by the corresponding route handlers.
* Run the application, apply migrations, and test every documented endpoint.
* Add automated tests for authentication, ownership checks, and database operations.

These are verification items, not claims that every issue is necessarily present in the current version.

## Future Improvements

Possible extensions that would strengthen the project include:

* Automated integration tests using an isolated test database
* Pagination, filtering, and sorting for post retrieval
* Improved centralized exception handling and structured logging
* Continuous integration for testing and code quality
* Docker-based local development
* Deployment configuration with secure secrets management
* More comprehensive API documentation and example requests

## Learning Outcomes

This project provides practical experience with:

* Designing RESTful endpoints with FastAPI
* Organizing a backend into routers and reusable dependencies
* Modeling relational data with SQLAlchemy and PostgreSQL
* Implementing JWT authentication and password hashing
* Validating API inputs and outputs with Pydantic
* Managing database changes with Alembic
* Exploring and testing APIs with Swagger UI and Postman

## Author

**Aaradhya Nikam**

* GitHub: [@aaradhya8nikam](https://github.com/aaradhya8nikam)
* Project: [fastapi_social_media_api](https://github.com/aaradhya8nikam/fastapi_social_media_api)

---

If you find a bug or have an improvement suggestion, feel free to open an issue or submit a pull request.
