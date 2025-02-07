### **📥 Importing Dummy Data into the Database**  

To populate your MySQL database with dummy data, follow these steps to import the provided **`phoneredirect.sql`** file using **MySQL Workbench** or the command line.

---

### **🔹 Method 1: Using MySQL Workbench (GUI)**
1. **Open MySQL Workbench** and connect to your database server.
2. **Create the database** (if not already created):
   ```sql
   CREATE DATABASE phoneredirect;
   ```
3. **Go to "Server" > "Data Import"**.
4. Select **"Import from Self-Contained File"**, then browse and select **`phoneredirect.sql`**.
5. Under **"Default Schema to be Imported To"**, select **`phoneredirect`**.
6. Click **"Start Import"** and wait for the process to complete.
7. **Verify the data**:
   ```sql
   USE phoneredirect;
   SELECT * FROM redirects;
   ```
   If records appear, the import was successful. ✅

---

### **🔹 Method 2: Using MySQL Command Line**
1. Open a terminal or command prompt.
2. **Log in to MySQL**:
   ```bash
   mysql -u root -p
   ```
   Enter your MySQL password when prompted.
3. **Create the database** (if not already created):
   ```sql
   CREATE DATABASE phoneredirect;
   ```
4. **Exit MySQL** by typing:
   ```sql
   EXIT;
   ```
5. **Import the SQL file** using:
   ```bash
   mysql -u root -p phoneredirect < /path/to/phoneredirect.sql
   ```
   *(Replace `/path/to/phoneredirect.sql` with the actual file path.)*
6. **Verify the import**:
   ```bash
   mysql -u root -p
   USE phoneredirect;
   SELECT * FROM redirects;
   ```
   If records appear, the data was successfully imported. ✅

---

### **🎯 Final Steps**
- Run the Django server:
  ```bash
  python manage.py runserver
  ```
- Visit the API:
  [http://127.0.0.1:8000/api/redirects/](http://127.0.0.1:8000/api/redirects/)
- The dummy data should now be accessible through the API.

---
