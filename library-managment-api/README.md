 Library Management API

This project is a **Flask-based RESTful API** to manage a collection of books in a library.

---

## Features
- Add, list, update, and delete books.
- Search books by **author**, **published year**, or **genre**.
- API documentation via Swagger UI.

---

## Getting Started

### Prerequisites
- Python 3.8 or above.
- Flask and required dependencies (install via `requirements.txt`).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/M-Abdeltawab/Bonus-Assignment.git
   cd Bonus-Assignment
   cd library-managment-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the API documentation at:
   ```
   http://localhost:5000/api-docs
   ```

---

## API Endpoints

### Books

1. **List all books**
   - `GET /books`
   - **Response:** Array of all books.

2. **Add a new book**
   - `POST /books`
   - **Request Body:**
     ```json
     {
       "title": "Book Title",
       "author": "Author Name",
       "published_year": 2023,
       "isbn": "1234567890",
       "genre": "Fiction"
     }
     ```

3. **Search books**
   - `GET /books/search?author=Name&published_year=2023&genre=Fiction`
   - **Query Parameters:** Optional (`author`, `published_year`, `genre`).

4. **Delete a book**
   - `DELETE /books/{isbn}`

5. **Update a book**
   - `PUT /books/{isbn}`
   - **Request Body:** Partial or full book object to update.

---

## Swagger Documentation
- Access the interactive API documentation at:
  ```
  http://localhost:5000/api-docs
  ```

---

## Data Persistence
Books data is stored in a local JSON file (`library.json`).

---