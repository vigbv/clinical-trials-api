# clinical_trials_api
Example API for clinical trial studies using Python - Django

Setting up Django:
mkdir clinical_trials_api
cd clinical_trials_api

# Create virtual python environment
python3 -m venv env
env\scripts\activate # Windows 
env/bin/activate # MAC or Linux 

# Install Django
pip install django
pip install djangorestframework

# Initialize database
python3 manage.py migrate

# Create super user
python3 manage.py createsuperuser

# Start server
python3 manage.py runserver

# To test post request
Users can post  json content from resources/covid_19_studies.json to create new db entries for new studies
