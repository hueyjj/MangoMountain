# MangoMountain
This repository holds the Django backend for [Skadoosh.](https://github.com/hueyjj/Skadoosh)

## Enable Virtual Environment
```
cd MangoMountain
virtualenv env
source env/Scripts/activate # Windows
```

## Install Requirements
- pip
- virtualenv
- postgresql
    - create database: skadoosh
- python 3

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

## Additional Usage
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

## Heroku 
```
heroku run python manage.py loaddata course_info_fixture.json # Load course data into database
```
```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
```

## API Routes
Create an account
- /api/signup (POST)
```
email - User email
password - User password
confirm_password - User password confirmation
```
Response: create account success status, invalid username/password/password confirmation status, or some uknown invalid status.

Login
- /api/login (POST)
```
email - User email
password - User password
```
Response: login success status, invalid credential status, or some unknown invalid status.

Logout
- /api/logout (POST)
```
<Send cookies>
```
Response: success or fail status

Profile
- /api/profile (POST)
```
<Send cookies>
```
Response: user data or fail status

Course
- /api/course (POST)
```
term - School term
status - Course status (open, closed, all)
subject - Course subject
course_num - Course number
course_title_key_word - Key words to search for
instructor_last_name - Instructor's last name
general_education - A general education option
course_units - How many course units to filter for
meeting_days - Specific days to search for
course_career - User course status (undergraduate/graduate)
```
Response: list of courses found in the database, or error if invalid form

Create Review
- /api/create_review (POST)
```
subject - Course subject
term - Course term
course_title - Course title
rating - Course rating
comment - User comments about the course
```
Response: success or fail status

Find Reviews
- /api/find_review (POST)
```
search_term - Key words to filter reviews by
```
Response: list of reviews found in the database, or error if invalid form