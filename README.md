
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

### `PUT /api/users/profile/update/`

**Description:**

Update user profile.

**Request:**
- **Method:** `PUT`
- **Endpoint:** `/api/users/profile/update/`
- **Header:** `Authorization: Bearer <access_token>`
- **Body:**
  - `bio` (string, optional): User's about.
  - `date_of_birth` (date, optional): User's date_of_birth.
  - `location` (string, optional): User's location.
  - `social_media_link` (string, optional): User's social media link.

**Response:**
- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "id": 1,
      "bio": "Updated bio content.",
      "date_of_birth": "1990-01-01",
      "location": "Updated location",
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


### `POST /api/books/create/`

**Description:**

Create a new book.

**Request:**
- **Method:** `POST`
- **Endpoint:** `/api/books/create/`
- **Header:** `Authorization: Bearer <access_token>`
- **Body:**
  - `title` (string, required): Title of the book.
  - `authors` (string, required): Authors of the book.
  - `genre` (string, required): Genre of the book.
  - `publication_date` (date, required): Publication date of the book.
  - `description` (string, optional): Description of the book.
  - `document` (file, optional): Document file of the book.

**Response:**
- **Success Response:**
  - **Status Code:** 201 Created
  - **Body:**
    ```json
    {
      "id": 1,
      "title": "Sample Book",
      "authors": "Author Name",
      "genre": "Fiction",
      "publication_date": "2024-05-05",
      "description": "Sample description",
      "document": "http://example.com/books/documents/sample_book.pdf"
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


### `GET /api/books/list/`

**Description:**

List all books related to the user.

**Request:**
- **Method:** `GET`
- **Endpoint:** `/api/books/list/`
- **Header:** `Authorization: Bearer <access_token>`

**Response:**
- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    [
      {
        "id": 1,
        "title": "Sample Book 1",
        "authors": "Author 1",
        "genre": "Fiction",
        "publication_date": "2023-01-01",
        "description": "Sample description 1",
        "document": "http://example.com/books/documents/sample_book_1.pdf"
      },
      {
        "id": 2,
        "title": "Sample Book 2",
        "authors": "Author 2",
        "genre": "Non-fiction",
        "publication_date": "2022-05-05",
        "description": "Sample description 2",
        "document": "http://example.com/books/documents/sample_book_2.pdf"
      }
    ]
    ```

- **Error Response:**
  - **Status Code:** 401 Unauthorized
  - **Body:**
    ```json
    {
      "error": "Unauthorized access. Please provide valid credentials."
    }
    ```


### `GET /api/books/list-all/`

**Description:**

List all books.

**Request:**
- **Method:** `GET`
- **Endpoint:** `/api/books/list-all/`

**Response:**
- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    [
      {
        "id": 1,
        "title": "Sample Book 1",
        "authors": "Author 1",
        "genre": "Fiction",
        "publication_date": "2023-01-01",
        "description": "Sample description 1",
        "document": "http://example.com/books/documents/sample_book_1.pdf"
      },
      {
        "id": 2,
        "title": "Sample Book 2",
        "authors": "Author 2",
        "genre": "Non-fiction",
        "publication_date": "2022-05-05",
        "description": "Sample description 2",
        "document": "http://example.com/books/documents/sample_book_2.pdf"
      }
    ]
    ```

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "No books found."
    }
    ```

### `PUT /api/books/update/<int:pk>/`

**Description:**

Update a specific book.

**Request:**
- **Method:** `PUT`
- **Endpoint:** `/api/books/update/<int:pk>/`
- **Header:** `Authorization: Bearer <access_token>`
- **Body:**
  - `title` (string, optional): Updated title of the book.
  - `authors` (string, optional): Updated authors of the book.
  - `genre` (string, optional): Updated genre of the book.
  - `publication_date` (date, optional): Updated publication date of the book.
  - `description` (string, optional): Updated description of the book.
  - `document` (file, optional): Updated document file of the book.

**Response:**
- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "id": 1,
      "title": "Updated Book Title",
      "authors": "Updated Author",
      "genre": "Updated Genre",
      "publication_date": "2024-01-01",
      "description": "Updated description",
      "document": "http://example.com/books/documents/updated_book.pdf"
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

### `DELETE /api/books/delete/<int:pk>/`

**Description:**

Delete a specific book.

**Request:**
- **Method:** `DELETE`
- **Endpoint:** `/api/books/delete/<int:pk>/`
- **Header:** `Authorization: Bearer <access_token>`

**Response:**
- **Success Response:**
  - **Status Code:** 204 No Content

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Book not found."
    }
    ```

### `POST /api/reading-list/create/`

**Description:**

Create a new reading list.

**Request:**
- **Method:** `POST`
- **Endpoint:** `/api/reading-list/create/`
- **Header:** `Authorization: Bearer <access_token>`
- **Body:**
  - `name` (string, required): Name of the reading list.
  - `books`(lists, required): Id of the books.
  - `order`(lists, optional): Integer numbers for ordering.

**Response:**
- **Success Response:**
  - **Status Code:** 201 Created
  - **Body:**
    ```json
    {
      "id": 1,
      "name": "Sample Reading List"
      "books":[ 1,2,3]
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

### `PUT /api/reading-list/update/<int:pk>/`

**Description:**

Update a specific reading list.

**Request:**
- **Method:** `PUT`
- **Endpoint:** `/api/reading-list/update/<int:pk>/`
- **Header:** `Authorization: Bearer <access_token>`
- **Body:**
  - `name` (string, opitional): Updated name of the reading list.
  - `books`(list, optional): Updated books of the reading list.

**Response:**
- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "id": 1,
      "name": "Updated Reading List Name"
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

### `GET /api/reading-list/all/`

**Description:**

List all reading lists related to the user.

**Request:**
- **Method:** `GET`
- **Endpoint:** `/api/reading-list/all/`
- **Header:** `Authorization: Bearer <access_token>`

**Response:**
- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    [
      {
        "id": 1,
        "name": "Sample Reading List"
      },
      {
        "id": 2,
        "name": "Another Reading List"
      }
    ]
    ```

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "No reading lists found."
    }
    ```

### `DELETE /api/reading-list/delete/<int:pk>/`

**Description:**

Delete a specific reading list related to the user.

**Request:**
- **Method:** `DELETE`
- **Endpoint:** `/api/reading-list/delete/<int:pk>/`
- **Header:** `Authorization: Bearer <access_token>`

**Response:**
- **Success Response:**
  - **Status Code:** 204 No Content

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Reading list not found."
    }
    ```

### `POST /api/reading-list/add-item/<int:reading_list_id>/`

**Description:**

Add a book to a reading list.

**Request:**
- **Method:** `POST`
- **Endpoint:** `/api/reading-list/add-item/<int:reading_list_id>/`
- **Header:** `Authorization: Bearer <access_token>`
- **Body:**
  - `book_id` (integer, required): ID of the book to add to the reading list.

**Response:**
- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "message": "Book added to reading list successfully."
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

### `DELETE /api/reading-list/<int:reading_list_id>/books/<int:book_id>/delete/`

**Description:**

Remove a book from a reading list.

**Request:**
- **Method:** `DELETE`
- **Endpoint:** `/api/reading-list/<int:reading_list_id>/books/<int:book_id>/delete/`
- **Header:** `Authorization: Bearer <access_token>`

**Response:**
- **Success Response:**
  - **Status Code:** 204 No Content

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Book not found in reading list."
    }
    ```

