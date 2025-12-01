# 🎬 Django Movie API

A simple and clean **Django + Django REST Framework** project that allows you to create, read, update, and delete movie details.  
This project is perfect for showcasing your **backend development** skills using Django and REST API.

---

## 🚀 Features

- Fully functional REST API  
- CRUD operations for movies  
- Clean and simple codebase  
- SQLite database (default)  
- Easy to run locally  
- Organized project structure

---

## 📂 Project Structure

django-movie-api/
│ manage.py
│ requirements.txt
│
├── movierater/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
└── api/
├── models.py
├── serializers.py
├── views.py
└── urls.py


---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/django-movie-api.git
cd django-movie-api


Create a virtual environment:

python -m venv venv


Activate the environment:

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

🔧 Apply Migrations
python manage.py migrate

▶️ Run the Server
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/api/movies/

🎬 API Endpoints
Method	Endpoint	Description
GET	/api/movies/	List all movies
POST	/api/movies/	Add a new movie
GET	/api/movies/{id}/	Get single movie details
PUT	/api/movies/{id}/	Update a movie
DELETE	/api/movies/{id}/	Delete a movie
🎥 Sample JSON for Adding a Movie
{
  "title": "RRR",
  "description": "Revolutionary action-drama epic directed by S.S. Rajamouli."
}

📌 Technologies Used

Python

Django

Django REST Framework

SQLite (default)

✨ Author

Your Name
Backend Developer | Python | Django
GitHub: https://github.com/your-username

⭐ Show Your Support

If you like this project, consider giving the repository a star ⭐ on GitHub!


---

If you want, I can also create a:

✅ `.gitignore` file  
✅ LICENSE file  
or  
✅ Add a "How to Deploy" section for Render / Railway  

Just tell me!
