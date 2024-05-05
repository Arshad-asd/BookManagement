
# Book Management System



This repository contains the source code for a Books Management System developed using Python Django REST Framework. The system handles Users authentication with Role based, user can mange users account and books.

## Table of Contents

- [Core Features](#core-features)

- [Setup & Running Instructions](#project-set-up-and-running)

- [API Endpoints](#api-endpoints)

- [API Documentation](#api-documentation)

- [Testing](#testing)

## Core Features


#### 1. Authentication & Profile Management:


The Content Management System users a token-based authentication system to secure API endpoints. This system enhances security and ensures that only authenticated users have access to sensitive operations. The authentication mechanism is based on JSON Web Tokens (JWT), providing a stateless and secure approach.


#### 2. Book Management :

Users should be able to create, remove, and upload books.
All users should be able to access all the books.Each book should have a title, author(s), genre, publication date, and an optional description.

#### 3. Reading Lists:


Users should be able to create and manage reading lists. Reading lists should allow users to organise their books in their preferred order.


## Project set up and running.

1. Clone the repository:

```bash
git clone https://github.com/Arshad-asd/BookManagement.git
```

2. Create and activate a virtual environment
   
```bash
python -m venv env
```
```bash
# On Windows: .\env\Scripts\activate
# On macOS/Linux: source venv/bin/activate
```
```bash
cd BookManagement
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a superuser for administrative access:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Access the API at [http://localhost:8000/api/](http://localhost:8000/api/)


## API Endpoints


#### 1. User Management:

- `POST /api/users/register/`: Register a new user.
- `POST /api/users/login/`: Log in an existing user.
- `POST /api/users/profile/create/`: Create user profile.
- `PUT /api/users/profile/update/`: Update user profile.

#### 2. Book Management:

- `POST /api/books/create/`: Create a new book.
- `GET /api/books/list/`: List all books related to the user.
- `GET /api/books/list-all/`: List all books.
- `PUT /api/books/update/<int:pk>/`: Update a specific book.
- `DELETE /api/books/delete/<int:pk>/`: Delete a specific book.

#### 3. Reading List Management:

- `POST /api/reading-list/create/`: Create a new reading list.
- `PUT /api/reading-list/update/<int:pk>/`: Update a specific reading list.
- `GET /api/reading-list/all/`: List all reading lists related to the user.
- `DELETE /api/reading-list/delete/<int:pk>/`: Delete a specific reading list related to the user.
- `POST /api/reading-list/add-item/<int:reading_list_id>/`: Add a book to a reading list.
- `DELETE /api/reading-list/<int:reading_list_id>/books/<int:book_id>/delete/`: Remove a book from a reading list.



## API Documentation


### `POST /api/user/register/`

**Description:**

Create a new User.

**Request:**
- **Method:** `POST`
- **Endpoint:** `/api/user/register/`
- **Body:**
  - `username` (string, required): User's username.
  - `email` (string, required): User's email.
  - `password` (string, required): User's password. "Password must be at least 6 characters long and contain at least one uppercase letter, one lowercase letter, and one digit."

**Response:**
- **Success Response:**
  - **Status Code:** 201 Created
  - **Body:**
    ```json
    {
      "id": 1,
      "email": "jhon@example.com"
      "username": "jhon"
    }
    ```

- **Error Response:**
  - **Status Code:** 400 Bad Request
  - **Body:**
    ```json
    {
      "error": "Invalid data. Please provide valid information."
    }
    ```

    ### `POST /api/login/`

**Request:**
- **Method:** `POST`
- **Endpoint:** `/api/login/`
- **Body:**
  - `email` (string, required): User's email.
  - `password` (string, required): User's password.

**Response:**
- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9...",
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9..."
    }
    ```

- **Error Response:**
  - **Status Code:** 401 Unauthorized
  - **Body:**
    ```json
    {
      "error": "Invalid credentials"
    }
    ```

### `POST /api/profile/create/`

**Request:**
- **Method:** `POST`
- **Endpoint:** `/api/profile/create/`
- **Header:** `Authorization: Bearer <access_token>`
- **Body:**
  - `bio` (string, required): User's about.
  - `date_of_birth` (date, required): User's date_of_birth.
  - `location` (string, required): User's location.
  - `social_media_link` (string, required): User's social_media_link.

**Response:**
- **Success Response:**
  - **Status Code:** 201 Created
  - **Body:**
    ```json
    {
      "id": 1,
      "bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
      "date_of_birth": "1990-01-01",
      "location": "New York, USA",
      "social_media_link": "https://example.com/user123"
    }
    ```

- **Error Response:**
  - **Status Code:** 400 Bad Request
  - **Body:**
    ```json
    {
      "error": "Invalid data. Please provide valid information."
    }
    ```
