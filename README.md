# Mentorship Website (Django) — Starter

## Quick Start
```bash
python -m venv .venv
# Windows: . .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py seed_students  # optional sample data
python manage.py runserver
```

Visit: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

## Notes
- Uses SQLite for local testing
- Bootstrap via CDN
- Student cards on homepage with a 'More students' list and detail pages
- Ready to switch `photo_url` to an `ImageField` later
