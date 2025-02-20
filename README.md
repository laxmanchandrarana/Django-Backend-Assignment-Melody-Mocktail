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
cd Django-Backend-Assignment-Melody-Mocktail
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
![image](https://github.com/user-attachments/assets/56c372d9-a619-42d7-95c4-7f1aa968e4de)

---

#### **B. Retrieve All Redirects (GET Request)**

1. Create a new request named **"Get All Redirects"**.
2. Select **GET** as the method.
3. **URL:** `http://127.0.0.1:8000/api/redirects/`
4. Click **Send**.

**Expected Result:**  
A **200 OK** response with all redirect objects in JSON format.
![image](https://github.com/user-attachments/assets/75e3c6b9-89b6-4ac1-a492-fa9e567e665f)

---

#### **C. Filter Redirects (GET with Query Parameters)**

1. Clone the **"Get All Redirects"** request or create a new one.
2. Select **GET** as the method.

**Filter by Active Status:**
- **URL:** `http://127.0.0.1:8000/api/redirects/?is_active=true`
![image](https://github.com/user-attachments/assets/42853d46-dc01-4c42-a6da-127bec78928a)

**Filter by Availability:**
- **URL:** `http://127.0.0.1:8000/api/redirects/?availability=web_only`
![image](https://github.com/user-attachments/assets/7a268bcc-9c4b-4471-9e86-fa21aec5b691)

**Sort by Position:**
- **URL:** `http://127.0.0.1:8000/api/redirects/?ordering=position`
![image](https://github.com/user-attachments/assets/f47028df-7d94-49a3-859a-86d4b5f7f79f)

3. Click **Send**.

**Expected Result:**  
The response should contain filtered or sorted results based on your query.
![image](https://github.com/user-attachments/assets/117c1f18-0ebf-44de-ab9e-8b3f0aaef6ec)

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
       "position": 1000,
       "is_active": false
     }
     ```

5. Click **Send**.

**Expected Result:**  
A **200 OK** response with the updated redirect data.
![image](https://github.com/user-attachments/assets/cff3a4e2-caa3-4e95-a47e-25cde12968d5)

---

#### **E. Delete a Redirect (DELETE Request)**

1. Create a new request named **"Delete Redirect"**.
2. Select **DELETE** as the method.
3. **URL:** `http://127.0.0.1:8000/api/redirects/1/` *(Replace `1` with the actual ID)*

4. Click **Send**.

**Expected Result:**  
A **204 No Content** response, indicating successful deletion.
![image](https://github.com/user-attachments/assets/2210b670-0ac1-42ea-844e-a3ddfd2958c5)

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

## 🧪 Unit Tests for APIs (Bonus)

This project includes **unit tests** to ensure API reliability and correctness. The test suite verifies:
- **CRUD operations** for redirects.
- **Image upload handling**.
- **Filtering and sorting functionality**.
- **Validation checks** for required fields.

### **Run Unit Tests**
To execute all unit tests, run the following command:
```bash
python manage.py test
```

### **Example Test Output**
```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.452s

OK
Destroying test database for alias 'default'...
```

The tests ensure that the API behaves as expected. 🛡️✅

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

This project fulfills all the requirements of the Django Backend Assignment. 🚀

---
## 🔗 Connect with Me

<p align="left">
  <a href="https://github.com/laxmanchandrarana" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  
  <a href="https://www.linkedin.com/in/laxmanchrana" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  
  <a href="[https://www.instagram.com/your-instagram-handle](https://www.instagram.com/laxmanchandrarana/)" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
  </a>

  <a href="[https://yourwebsite.com](https://laxman.rf.gd/)" target="_blank">
    <img src="https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=About.me&logoColor=white" alt="Website">
  </a>

  <a href="mailto:lcr.acw@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
</p>


**Author:** *Laxman Chandra Rana*   
```
