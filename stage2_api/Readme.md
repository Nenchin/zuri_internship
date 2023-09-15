# Zuri Task API Documentation

The Zuri Task API is a simple Flask-based RESTful API for managing information about users. It provides endpoints for creating, retrieving, updating, and deleting user records.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Get User by ID](#get-User-by-id)
  - [Update User by ID](#update-a-by-id)
  - [Delete User by ID](#delete-User-by-id)
  - [Create User](#create-User)
- [Request/Response Formats](#requestresponse-formats)
  - [Get User by ID (GET)](#get-User-by-id-get-request)
  - [Update User by ID (PUT)](#update-User-by-id-put-request)
  - [Delete User by ID (DELETE)](#delete-User-by-id-delete-request)
  - [Create User (POST)](#create-User-post-request)
- [Sample Usage](#sample-usage)
- [License](#license)

## Project Overview

The Zuri Task API is built using Flask, a lightweight web framework for Python. It allows you to perform CRUD (Create, Read, Update, Delete) operations on user records. user records have two attributes: `name`.

## Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (>= 3.6)
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Nenchin/zuri_internship/tree/master/stage2_api.git
   cd stage2_api

2. Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate

3. Install the required dependencies:
    pip install Flask Flask-SQLAlchemy marshmallow-sqlalchemy

4. Create the SQLite database:
    python
>>> from app import db
>>> db.create_all()
>>> exit()

5. Run the application:
    python app.py

The API should now be running locally at http://localhost:5000

API Endpoints
Get user by ID (GET)
    Endpoint: GET /users/<int:id>
    Description: Retrieve an user by their unique ID.
    Response Format:
        JSON object with the following fields:
            id (integer): The unique ID of the user.
            name (string): The name of the user.

Update user by ID (PUT)
    Endpoint: PUT /users/<int:id>
    Description: Update an user's details by their ID.
    Request Format:
        JSON object with one or both of the following fields:
            name (string): The updated name of the user.
            
    Response Format:
        JSON object with the updated user details (same format as "Get user by ID").
Delete user by ID (DELETE)
    Endpoint: DELETE /users/<int:id>
    Description: Delete an user by their ID.
    Response Format: An empty response with a status code 204 (No Content) on success.

Create user (POST)
    Endpoint: POST /users
    Description: Create a new user.
    Request Format:
        JSON object with the following required fields:
            name (string): The name of the user.
    Response Format:
        JSON object with the newly created user's details (same format as "Get user by ID").


Sample Usage
Get user by ID (GET Request)
curl http://localhost:5000/users/1

Update user by ID (PUT Request)
curl -X PUT http://localhost:5000/users/1 -H "Content-Type: application/json" -d '{
  "name": "Updated name"
}'

Delete user by ID (DELETE Request)
curl -X DELETE http://localhost:5000/users/1

Create user (POST Request)
curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d '{
  "name": "John Doe"
}'




This comprehensive documentation provides all the necessary information for users to set up, understand,
and use your Zuri Task API effectively. Make sure to give me a star.
