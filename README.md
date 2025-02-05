Here’s the complete `README.md` code ready for your GitHub repository:

```markdown
# 📱 Django Phone Redirect API

This Django REST API provides **CRUD** functionality for managing redirect objects with image uploads, filtering, sorting, and robust validation. It supports redirects for both web and phone, with flexible availability options and position-based ordering.

---

## 🚀 Features

- **CRUD Operations**: Create, Read, Update, and Delete redirect records.
- **Image Uploads**: Upload separate images for phone and web views.
- **Sorting & Filtering**:
  - Sort by `position` (ascending by default).
  - Filter by `is_active` status and `availability` (`web_only`, `phone_only`, `both`).
- **MySQL Database**: Uses MySQL for efficient data management.
- **Admin Panel**: Manage records via Django Admin.
- **Unit Tests**: Full test coverage for API endpoints.

---

## 🛠️ Setup Instructions

### 1. **Clone the Repository**
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd phone_redirect_api
```

### 2. **Create and Activate Virtual Environment**
```bash
python -m venv venv
# For Windows
venv\Scripts\activate
# For Mac/Linux
source venv/bin/activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Configure MySQL Database**

Ensure MySQL is running on your machine.

- Create a database named `phoneredirect`:
```sql
CREATE DATABASE phoneredirect;
```

- Update `phone_redirect_api/settings.py` with your MySQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'phoneredirect',
        'USER': 'root',  # Replace with your MySQL username
        'PASSWORD': 'your_password',  # Replace with your MySQL password
        'HOST': 'localhost',
        'PORT': '3308',  # Update port if necessary
    }
}
```

### 5. **Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Create Superuser (For Admin Panel)**
```bash
python manage.py createsuperuser
```

### 7. **Run the Server**
```bash
python manage.py runserver
```

Visit the API at: [http://127.0.0.1:8000/api/redirects/](http://127.0.0.1:8000/api/redirects/)

Visit the Admin panel at: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🧪 Testing the API

### **Run Unit Tests**
```bash
python manage.py test
```

### **Test API with Postman or cURL**

#### 1. **Create a Redirect (POST)**
```bash
curl -X POST http://127.0.0.1:8000/api/redirects/ \
  -F "title_web=New Web" \
  -F "title_phone=New Phone" \
  -F "position=1" \
  -F "is_active=true" \
  -F "availability=both" \
  -F "redirect_url_web=http://example.com/web" \
  -F "redirect_url_phone=http://example.com/phone" \
  -F "image_web=@/path/to/web_image.jpg" \
  -F "image_phone=@/path/to/phone_image.jpg"
```

#### 2. **Get Redirects (GET)**
```bash
curl -X GET http://127.0.0.1:8000/api/redirects/
```

#### 3. **Filter Redirects (GET)**
- **Filter by Active Status**:
```bash
curl -X GET "http://127.0.0.1:8000/api/redirects/?is_active=true"
```
- **Filter by Availability**:
```bash
curl -X GET "http://127.0.0.1:8000/api/redirects/?availability=web_only"
```
- **Sort by Position**:
```bash
curl -X GET "http://127.0.0.1:8000/api/redirects/?ordering=position"
```

#### 4. **Update a Redirect (PUT)**
```bash
curl -X PUT http://127.0.0.1:8000/api/redirects/1/ \
  -H "Content-Type: application/json" \
  -d '{"title_web": "Updated Web", "position": 2, "is_active": false}'
```

#### 5. **Delete a Redirect (DELETE)**
```bash
curl -X DELETE http://127.0.0.1:8000/api/redirects/1/
```

---

## 📝 API Endpoints

| Method | Endpoint                     | Description                      |
|--------|------------------------------|----------------------------------|
| GET    | `/api/redirects/`            | Retrieve all redirects           |
| POST   | `/api/redirects/`            | Create a new redirect            |
| GET    | `/api/redirects/<id>/`       | Retrieve a specific redirect     |
| PUT    | `/api/redirects/<id>/`       | Update a specific redirect       |
| DELETE | `/api/redirects/<id>/`       | Delete a specific redirect       |

---

## 🛡️ Technologies Used

- **Django** - Web framework
- **Django REST Framework** - API development
- **MySQL** - Relational database
- **Pillow** - Image processing
- **Postman / cURL** - API testing
- **Unit Tests** - API test coverage with Django’s testing framework

---

## 🎯 Assignment Requirements

- [x] **CRUD Endpoints** implemented with Django REST Framework.
- [x] **Sorting & Filtering** by `position`, `is_active`, and `availability`.
- [x] **MySQL Database** setup and configured.
- [x] **Validation & Error Handling** included in serializers.
- [x] **Django Admin Panel** for managing records.
- [x] **Unit Tests** for all CRUD operations and edge cases.

---

## 🔗 Submission

This project fulfills all the requirements of the Django Backend Assignment for the internship application. 🚀

---

**Author:** *[Your Name]*  
**GitHub:** *[Your GitHub Profile Link]*  
```

---

### **What to Do Next:**

1. **Replace** `<YOUR_GITHUB_REPO_URL>` with your repository URL.
2. **Customize** the **Author** and **GitHub** sections with your name and profile link.
3. **Optional:** Add screenshots or API response examples if you'd like to make it more visually appealing.

You're all set to submit this polished project! 🚀 Let me know if you need further tweaks or help with anything else. 💪
