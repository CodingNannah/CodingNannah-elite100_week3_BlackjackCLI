# Star Wars cards! https://github.com/kimuraz/api-sw-cards
# If this does not work, could scan png & add images folder to create own cards.

# get API called
# consider how to modify code: do what with cards?

# API uses Django - no time to learn that right now.

import requests
url_starwars = 'https://github.com/kimuraz/api-sw-cards'
response = requests.get(url_starwars)
data = response.json()
print(response)

"""
Install: 
pip install -r requirements.txt

Requirements.txt ==
Django==1.11
django-cors-headers==2.1.0
djangorestframework==3.7.7
Markdown==2.6.11
pytz==2017.3

Setting Database:
./manage.py makemigrations
./manage.py migrate
./manage.py loaddata cards.json

Running server:
./manage.py runserver"""
