# 🐍 BlogNest API – Django REST Framework

The **BlogNest API** is the backend service powering the BlogNest social blogging platform.  
Built with **Django REST Framework** and deployed on **Render**, it provides secure, scalable, and efficient endpoints for authentication, blog management, user interactions, and social features.

---

## 🚀 Overview

BlogNest API solves the problem of managing user-generated content and social interactions in modern blogging applications. It offers a clean, well-structured backend that handles user accounts, blog posts, comments, likes, bookmarks, and more.  
Designed with scalability and performance in mind, the API ensures smooth communication with the BlogNest React UI.

---

## ✨ Features

- 🔐 **User Authentication & Authorization**  
- 📝 **Create, Read, Update & Delete (CRUD) for Blogs**  
- 💬 **Commenting System**  
- 👍 **Like & Bookmark Functionality**  
- 👤 **User Profiles & Post Filtering**  
- 🔍 **Search and Filtering Endpoints**  
- 🔄 **Pagination, Ordering & Throttling**  
- 🛡️ **Clerk Auth based security **  
- 🌍 **Fully deployed on Render**

---

## 🛠️ Tech Stack

### **Backend**
- **Python 3**
- **Django REST Framework**
- **Django ORM**
- 

### **Deployment**
- **Render Web Service**
- Auto-deploy via GitHub repo

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AlokPy1484/BlogNestAPI.git
cd blognest-api

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py runserver 
