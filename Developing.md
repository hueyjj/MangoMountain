## Enable Virtual Environment
```
cd MangoMountain
virtualenv env
source env/Scripts/activate # Windows
```

## Install Requirements
```
pip install -r requirements.txt
```
```
pip freeze > requirements.txt # Save requirements
```

## Usage
```
python manage.py runserver # Starts the server
```
```
python manage.py createsuperuser # Creates user with all privileges and permissions
```
```
python manage.py makemigration # Save changes for model
```
```
python manage.py migrate # Migrate database
```

## Django Setup
```
django-admin startproject PROJECT_NAME # Create django application
```
```
python manage.py startapp APP_NAME # Create Django app
```


## API Routes
Login
- /api/login (POST)
```
username - User username
password - User password
```
Response: login success status, invalid credential status, or some unknown invalid status.

Create an account
- /api/create-account (POST)
```
username - User username
password - User password
password_confirm - User password confirmation
```
Response: create account success status, invalid username/password/password confirmation status, or some uknown invalid status.
