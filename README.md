# Django REST Framework Blog API

This is a simple Django REST API for user registration, profile management, and blog CRUD operations. It supports authenticated user actions using JWT and allows users to manage their own blog posts.

---

## 🚀 Features
- User registration
- User profile update
- Create, read, update, delete blogs
- Authenticated endpoints using JWT
- Ownership protection on blog update/delete

---

## 🛠 Technologies Used
- Python 3.12
- Django
- Django REST Framework
- [django-decouple](https://pypi.org/project/python-decouple/) (for environment variables)

---

## 📁 Project Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create a virtual environment
```bash
mkvirtualenv rest_api_env
```

Or (if not using virtualenvwrapper):
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in your root directory:
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3  # or your PostgreSQL URL
```

### 5. Apply migrations and run server
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🔐 API Authentication
This project uses **JWT (JSON Web Tokens)**. To use authenticated routes:
1. Log in via a JWT auth endpoint (you can add `/api/token/` from `rest_framework_simplejwt`)
2. Use the token in Postman or frontend requests:
```
Authorization: Bearer <your-access-token>
```

---

## 📮 API Endpoints

### 👤 User
| Method | Endpoint           | Description                |
|--------|--------------------|----------------------------|
| POST   | `/register/`       | Register a new user        |
| PUT    | `/update-profile/` | Update authenticated user's profile |

### 📝 Blog
| Method | Endpoint             | Description                          |
|--------|----------------------|--------------------------------------|
| POST   | `/create-blog/`      | Create a new blog (auth required)    |
| GET    | `/blogs/`            | List all blogs                       |
| PUT    | `/update-blog/<id>/` | Update a blog (must be the author)   |
| DELETE | `/delete-blog/<id>/` | Delete a blog (must be the author)   |

---

## 🧾 Sample `requirements.txt`
```txt
django
djangorestframework
django-decouple
djangorestframework-simplejwt
Pillow  # for image upload
python-decouple
```

---

## ✅ Notes
- Make sure your media files (e.g., `profile_picture`) are properly handled in settings and URLs.
- Secure your production settings (disable debug, use PostgreSQL, add CORS, etc.).
- Use `serializer.save(partial=True)` if you want to support PATCH operations.

---

## 🧑 Author
Built by Alex Dev — feel free to fork, extend, and use.

---

Let me know if you'd like a Swagger/OpenAPI schema or Postman collection export!

