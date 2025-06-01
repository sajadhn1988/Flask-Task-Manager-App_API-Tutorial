
==========================================================
# 🚀 How to run the Task App APIs with Flask (Version 2):
==========================================================

## 🧱 Step 1: Set Up a Virtual Environment:

🔹 **Create the virtual environment** 
C:\Users\s\Desktop\flask-app> python -m venv venv

🔹 **Activate the virtual environment** 
C:\Users\s\Desktop\flask-app> venv\Scripts\activate

(venv) PS C:\Users\s\Desktop\flask-app> 
_____________________________________________________

## 📋 Step 2: Adding new requirement Packages:

(venv) PS C:\Users\s\Desktop\flask-app> pip install -r requirements.txt
_____________________________________________________

## 🧿 Step 3: Running the Flask app
(venv) PS C:\Users\s\Desktop\flask-app> python app.py
_____________________________________________________

## 🌐 Step 4: API Calls (With ThunderClient or Postman):

POST http://localhost:5000/users/register

JSON: 

{
  "username": "user1",
  "password": "sajad123"
}

Note: You need to go to the database and make one of the user's role admin manually
_______________________________________________________

POST http://localhost:5000/users/login

JSON: 
{
  "username": "user1",
  "password": "sajad123"
}
_______________________________________________________

GET http://localhost:5000/users/admin-user-list

Headers:

Authorization    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0ODc1MjgzNiwianRpIjoiZWE3YWFmNzAtNmMzMi00YzdiLTljOGItOTJiYWYyNTMwNmNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NDg3NTI4MzYsImNzcmYiOiJmMjBkMGY3Yy05NGQ1LTQ1M2UtODY4Yy01YWVmNmE4YjEwNjkiLCJleHAiOjE3NDg3NTM3MzYsInJvbGUiOiJhZG1pbiJ9.NQcc3z0rHHrC74qtqoL8eiQ2RGF63zXiLDDeydSENHk

Notes: the long string is the token from login API call
_______________________________________________________

PUT http://localhost:5000/users/update-role/4

JSON: 
{
  "role": "admin"
}

Authorization    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0ODc1MjgzNiwianRpIjoiZWE3YWFmNzAtNmMzMi00YzdiLTljOGItOTJiYWYyNTMwNmNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NDg3NTI4MzYsImNzcmYiOiJmMjBkMGY3Yy05NGQ1LTQ1M2UtODY4Yy01YWVmNmE4YjEwNjkiLCJleHAiOjE3NDg3NTM3MzYsInJvbGUiOiJhZG1pbiJ9.NQcc3z0rHHrC74qtqoL8eiQ2RGF63zXiLDDeydSENHk

Notes: the number 4 is the user id we want to update roles
_______________________________________________________

DELETE http://localhost:5000/users/delete/4

Authorization    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0ODc1MjgzNiwianRpIjoiZWE3YWFmNzAtNmMzMi00YzdiLTljOGItOTJiYWYyNTMwNmNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NDg3NTI4MzYsImNzcmYiOiJmMjBkMGY3Yy05NGQ1LTQ1M2UtODY4Yy01YWVmNmE4YjEwNjkiLCJleHAiOjE3NDg3NTM3MzYsInJvbGUiOiJhZG1pbiJ9.NQcc3z0rHHrC74qtqoL8eiQ2RGF63zXiLDDeydSENHk

Notes: Deleting the user with id 4
==========================================================

POST http://localhost:5000/tasks/create

Authorization    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0ODc1MjgzNiwianRpIjoiZWE3YWFmNzAtNmMzMi00YzdiLTljOGItOTJiYWYyNTMwNmNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NDg3NTI4MzYsImNzcmYiOiJmMjBkMGY3Yy05NGQ1LTQ1M2UtODY4Yy01YWVmNmE4YjEwNjkiLCJleHAiOjE3NDg3NTM3MzYsInJvbGUiOiJhZG1pbiJ9.NQcc3z0rHHrC74qtqoL8eiQ2RGF63zXiLDDeydSENHk

JSON: 
{
  "title": "New Task 1",
  "description": "This is the 1st task description",
  "status": "pending"
}

Note: Only ['admin', 'editor'] can use this API
_______________________________________________________

PUT http://localhost:5000/tasks/update/1

Authorization    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0ODc1MjgzNiwianRpIjoiZWE3YWFmNzAtNmMzMi00YzdiLTljOGItOTJiYWYyNTMwNmNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NDg3NTI4MzYsImNzcmYiOiJmMjBkMGY3Yy05NGQ1LTQ1M2UtODY4Yy01YWVmNmE4YjEwNjkiLCJleHAiOjE3NDg3NTM3MzYsInJvbGUiOiJhZG1pbiJ9.NQcc3z0rHHrC74qtqoL8eiQ2RGF63zXiLDDeydSENHk

JSON: 
{
  "title": "New Task 1",
  "description": "This is the 1st task description - Modified",
  "status": "completed"
}

Note: Only ['admin', 'editor'] can use this API
_______________________________________________________

GET http://localhost:5000/tasks/get-all

Authorization    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0ODc1MjgzNiwianRpIjoiZWE3YWFmNzAtNmMzMi00YzdiLTljOGItOTJiYWYyNTMwNmNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NDg3NTI4MzYsImNzcmYiOiJmMjBkMGY3Yy05NGQ1LTQ1M2UtODY4Yy01YWVmNmE4YjEwNjkiLCJleHAiOjE3NDg3NTM3MzYsInJvbGUiOiJhZG1pbiJ9.NQcc3z0rHHrC74qtqoL8eiQ2RGF63zXiLDDeydSENHk

Results:
[
  {
    "created_at": "2025-06-01T05:15:26.114205",
    "description": "This is the 1st task description - Modified",
    "id": 1,
    "status": "completed",
    "title": "New Task 1"
  },
  {
    "created_at": "2025-06-01T05:23:28.469182",
    "description": "This is the 2nd task description",
    "id": 2,
    "status": "pending",
    "title": "New Task 2"
  },
  {
    "created_at": "2025-06-01T05:23:39.239028",
    "description": "This is the 3rd task description",
    "id": 3,
    "status": "pending",
    "title": "New Task 3"
  }
]

Note: All users ['admin', 'editor', 'viewer'] can see all the tasks
_______________________________________________________

DELETE http://localhost:5000/tasks/delete/4

Authorization    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0ODc1MjgzNiwianRpIjoiZWE3YWFmNzAtNmMzMi00YzdiLTljOGItOTJiYWYyNTMwNmNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NDg3NTI4MzYsImNzcmYiOiJmMjBkMGY3Yy05NGQ1LTQ1M2UtODY4Yy01YWVmNmE4YjEwNjkiLCJleHAiOjE3NDg3NTM3MzYsInJvbGUiOiJhZG1pbiJ9.NQcc3z0rHHrC74qtqoL8eiQ2RGF63zXiLDDeydSENHk

Note: Only ['admin'] can use this API
_______________________________________________________

Happy Coding ❤️

==========================================================
# 🚀 How to Create a Flask App (Version 1):
==========================================================

## 🧱 Step 1: Set Up a Virtual Environment:

🔹 **Create the virtual environment** 
C:\Users\s\Desktop\flask-app> python -m venv venv

🔹 **Activate the virtual environment** 
C:\Users\s\Desktop\flask-app> venv\Scripts\activate
(venv) PS C:\Users\s\Desktop\flask-app> 
____________________________________________________

## 📝 Step 2: Create the app.py File:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is a Flask app"

if __name__ == "__main__":
    app.run(debug=True)

____________________________________________________

## 🔧 Step 3: Install Flask and Other Tools

🔹 **Update pip**
(venv) PS C:\Users\s\Desktop\flask-app> python.exe -m pip install --upgrade pip

🔹 **Create Flask APP**
(venv) PS C:\Users\s\Desktop\flask-app> pip install Flask

🔹 **Create a requirement file list**
(venv) PS C:\Users\s\Desktop\flask-app> pip freeze > requirements.txt 

🔹 **Running the Flask app**
(venv) PS C:\Users\s\Desktop\flask-app> python app.py

🔹 **Visit the address for the result**
Running on http://127.0.0.1:5000

____________________________________________________

## 🌐 Step 4: visiting the page http://127.0.0.1:5000

This is a Flask app

____________________________________________________

## 📂Step 5: Create a .gitignore File

🔹 Create a .gitignore file
In the root of your project directory (.\flask-app), create a file named .gitignore to exclude the virtual environment and other unnecessary files from version control. 

____________________________________________________

## Final Notes:

🔁 You can stop the server with Ctrl + C

🗂 Keep your code organized in folders like /templates, /static, etc. as your app grows

📦 To share your app: share your code + requirements.txt

🧡 Happy Coding with Flask!
