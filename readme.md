# Create virtual environment
Python should be 3.11

python3 -m venv env

# Activate virtual environment
source env/bin/activate or env\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Runserver - django
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver

# API Documentation
Link: https://docs.google.com/document/d/12dYRwP9yzRtv94dThMGa87HgsCcksTQ6dZjH5YtAJYU/edit?usp=sharing
