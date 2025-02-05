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
git clone https://github.com/laxmanchandrarana/Django-Backend-Assignment-Melody-Mocktail.git
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
![image](https://github.com/user-attachments/assets/205c7ccd-48c9-4996-8c94-724b84792465)

---

## 📬 Testing API with Postman

Follow these steps to test your Django API using **Postman**.

### **1. Setup Postman**

1. Download and install Postman: [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
2. Launch Postman and create a new collection named **"Django Redirect API"**.

---

### **2. CRUD Operations**

---

#### **A. Create a Redirect (POST Request)**

1. Click **New** > **Request**.
2. Name it **"Create Redirect"** and save it to your collection.
3. Select **POST** as the method.
4. **URL:** `http://127.0.0.1:8000/api/redirects/`
5. Go to the **Body** tab:
   - Select **form-data**.
   - Add the following fields:
     | Key               | Value                             | Type  |
     |-------------------|-----------------------------------|-------|
     | title_web         | My Web Title                      | Text  |
     | title_phone       | My Phone Title                    | Text  |
     | position          | 1                                 | Text  |
     | is_active         | true                              | Text  |
     | availability      | both                              | Text  |
     | redirect_url_web  | http://example.com/web            | Text  |
     | redirect_url_phone| http://example.com/phone          | Text  |
     | image_web         | *(Select an image file)*          | File  |
     | image_phone       | *(Select an image file)*          | File  |

6. Click **Send**.

**Expected Result:**  
A **201 Created** response with the submitted redirect data.

---

#### **B. Retrieve All Redirects (GET Request)**

1. Create a new request named **"Get All Redirects"**.
2. Select **GET** as the method.
3. **URL:** `http://127.0.0.1:8000/api/redirects/`
4. Click **Send**.

**Expected Result:**  
A **200 OK** response with all redirect objects in JSON format.

---

#### **C. Filter Redirects (GET with Query Parameters)**

1. Clone the **"Get All Redirects"** request or create a new one.
2. Select **GET** as the method.

**Filter by Active Status:**
- **URL:** `http://127.0.0.1:8000/api/redirects/?is_active=true`

**Filter by Availability:**
- **URL:** `http://127.0.0.1:8000/api/redirects/?availability=web_only`

**Sort by Position:**
- **URL:** `http://127.0.0.1:8000/api/redirects/?ordering=position`

3. Click **Send**.

**Expected Result:**  
The response should contain filtered or sorted results based on your query.

---

#### **D. Update a Redirect (PATCH Request)**

1. Create a new request named **"Update Redirect"**.
2. Select **PATCH** as the method.
3. **URL:** `http://127.0.0.1:8000/api/redirects/1/` *(Replace `1` with the actual ID)*
4. Go to the **Body** tab:
   - Select **raw** and choose **JSON**.
   - Enter the following:
     ```json
     {
       "title_web": "Updated Web Title",
       "position": 2,
       "is_active": false
     }
     ```

5. Click **Send**.

**Expected Result:**  
A **200 OK** response with the updated redirect data.

---

#### **E. Delete a Redirect (DELETE Request)**

1. Create a new request named **"Delete Redirect"**.
2. Select **DELETE** as the method.
3. **URL:** `http://127.0.0.1:8000/api/redirects/1/` *(Replace `1` with the actual ID)*

4. Click **Send**.

**Expected Result:**  
A **204 No Content** response, indicating successful deletion.

---

## 📝 API Endpoints

| Method | Endpoint                     | Description                      |
|--------|------------------------------|----------------------------------|
| GET    | `/api/redirects/`            | Retrieve all redirects           |
| POST   | `/api/redirects/`            | Create a new redirect            |
| GET    | `/api/redirects/<id>/`       | Retrieve a specific redirect     |
| PATCH  | `/api/redirects/<id>/`       | Update a specific redirect       |
| DELETE | `/api/redirects/<id>/`       | Delete a specific redirect       |

---

## 🛡️ Technologies Used

- **Django** - Web framework
- **Django REST Framework** - API development
- **MySQL** - Relational database
- **Pillow** - Image processing
- **Postman** - API testing
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

**Author:** *Laxman Chandra Rana*  
**GitHub:** [https://github.com/laxmanchandrarana](https://github.com/laxmanchandrarana)  
```