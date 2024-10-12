# BankAPI

This is a simple API for managing bank accounts, built using FastAPI.

## Project Structure

```plaintext
Banking Test/
└── BankAPI/
    ├── app/
    │   ├── main.py
    │   ├── models.py
    │   ├── schemas.py
    │   ├── database.py
    │   ├── routes/
    │   │   ├── __init__.py
    │   │   ├── accounts.py
    │   │   └── auth.py
    │   └── utils/
    │       ├── __init__.py
    │       └── auth.py
    └── bank.db
```
Requirements:

    Python 3.9+
    FastAPI
    Uvicorn
    SQLAlchemy (for ORM)
    Passlib (for password hashing)
    SQLite (or other database engines)

Installation:

    Clone the Repository:
    
    -bash
    -git clone https://github.com/yourusername/bank-api.gi
    -cd bank-api

Create a Virtual Environment:

It's recommended to create a virtual environment to manage dependencies.

    bash

    python -m venv venv

Then, activate it:

   -On Windows:

    bash

    .\venv\Scripts\activate

   -On Linux:

    bash

    source venv/bin/activate

Install Dependencies:

Install the required packages using pip:

    bash

    pip install -r requirements.txt

If you don't have a requirements.txt file yet, you can create it manually using:

    bash

    pip install fastapi uvicorn sqlalchemy passlib

Then, save the installed packages to the requirements.txt file:

    bash

    pip freeze > requirements.txt

Running the API

   Start the FastAPI Server:

   -After setting up the project and installing the dependencies, you can run the FastAPI server using Uvicorn:

    bash

    uvicorn app.main:app --reload

The --reload flag allows the server to restart automatically when code changes.

Access the API:

Once the server is running, you can access the API via:

    Swagger UI (API documentation): http://127.0.0.1:8000/docs

Make Requests:

You can interact with the API using tools like Postman or curl.

Example for creating an account using Postman:

    URL: http://127.0.0.1:8000/accounts/

    Method: POST

    Body: (JSON format)

    json:

        {
          "name": "John Doe",
          "balance": 1000
        }

File Overview

    app/main.py: Entry point for the FastAPI application. It includes the routes and sets up the FastAPI instance.
    app/models.py: Defines database models (using SQLAlchemy).
    app/schemas.py: Defines Pydantic schemas for request/response validation.
    app/database.py: Manages the database connection and session.
    app/routes/accounts.py: Contains the routes related to account management.
    app/routes/auth.py: Contains authentication routes (e.g., login, signup).
    app/utils/auth.py: Utility functions for authentication, like password hashing.

Additional Information

    Database: The project uses SQLite as the default database. The database file is bank.db. If you wish to switch to another database (e.g., PostgreSQL, MySQL), you'll need to update the database connection string in app/database.py.
    Authentication: Password hashing is done using Passlib.

Troubleshooting

If you encounter issues while running the application:

    404 Not Found: Check that the route you are trying to access exists in accounts.py and that it has been included in main.py.
    Module Not Found: Ensure all necessary dependencies are installed by running pip install -r requirements.txt.

License

This project is licensed under the MIT License. See the LICENSE file for details.
