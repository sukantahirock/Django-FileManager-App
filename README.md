# Django-FileManager-App

# Django File Manager Web Application

This is a Django-based web application that allows authenticated users to manage their personal file uploads securely. Users can upload, view, download, and delete their own files (PDFs, DOCX, images, etc.). Additionally, the admin has full access to view and delete all uploaded files.

## 🔑 Features

- 🔐 User authentication (login/register)
- 📤 Upload support for PDFs, DOCX, images, etc.
- 📁 View list of uploaded files (user-specific)
- 📥 Download uploaded files
- ❌ Delete own files
- 🛡️ Admin can view and delete all uploaded files
- 📬 Welcome email on registration (optional)
- 🧾 Full audit logging using Django signals (optional extension)

## ⚙️ Technologies Used

- Python 3.x
- Django 4.x
- SQLite3 (default) or PostgreSQL
- Bootstrap 5 (for frontend styling)
- Django messages framework

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Django-FileManager-App.git
   cd Django-FileManager-App
