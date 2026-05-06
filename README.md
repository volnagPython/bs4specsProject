# May 1, 2026
# Phone Specifications Django Project

## Description
Django project that runs a BeautifulSoup script to collect phone specifications
and stores them in PostgreSQL.

## Tech stack
- Python
- Django
- beautifulsoup4
- PostgreSQL

## Setup
```bash
git clone https://github.com/volnagPython/bs4specsProject.git
cd bs4specsProject
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
beautifulsoup4 install
python manage.py migrate
python manage.py runserver



