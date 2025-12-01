# DjangoMovieAPI

Minimal Django + Django REST Framework project (ready-to-run).

## Quick start (VS Code)

1. Create & activate a virtual environment:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - macOS / Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations and create superuser:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. API endpoints:
   - List/Create movies: GET/POST  http://127.0.0.1:8000/api/movies/
   - Retrieve movie: GET          http://127.0.0.1:8000/api/movies/<id>/
   - Rate a movie: POST           http://127.0.0.1:8000/api/movies/<id>/rate/
     Body example:
     {
         "rating": 5,
         "review": "Amazing!"
     }

Enjoy! ✨
