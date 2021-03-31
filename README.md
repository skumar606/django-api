# django-api

### Hosted on heroku => https://django-api-46.herokuapp.com/

## steps to run project locally

1. Clone the project `git clone https://github.com/skumar606/django-api.git`
2. Create virtual environment `pipenv shell`
3. Install the project dependencies `pip install -r requirements.txt`
4. `python manage.py makemigrations`
5. `python manage.py migrate`
6. `python manage.py runserver`


## rest api structure

1. Create a new user => POST req to https://django-api-46.herokuapp.com/api/users/ with json body {"username": "user123", "password": "123456"}
2. Get list of all users => GET res to https://django-api-46.herokuapp.com/api/users/ 
3. Generate jwt token and login => POST req to https://django-api-46.herokuapp.com/api/token/ with json body {"username": "user01", "password": "123456"}
4. Get profile info when logged in using jwt token => GET req to https://django-api-46.herokuapp.com/api/profile/
