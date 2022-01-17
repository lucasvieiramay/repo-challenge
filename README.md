# ClickSign challenge app 

This is an technical test for Clicksign python developer job

**Python 3.9, Django 4**


## Deploy to Heroku

You can deploy this app yourself to Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Building

It is best to use the python `pyenv` tool to build locally:

```sh
$ pyenv install 3.9.0
$ pyenv virtualenv 3.9.0 clicksign
$ pyenv activate clicksign
$ pip install -r requirements.txt
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. Alternatively you
can use foreman and gunicorn to run the server locally (after copying
`dev.env` to `.env`):

Don't forget to set your own `.env` file at the project's root
```sh
DEBUG=True
SECRET_KEY=django-insecure-x!+9pi5cipa(ehg6ljfd_w&emzbtbmp$hp-jjlkix9+dz_pimg
DATABASE_URL=sqlite://///Users/yourname/projects/clicksign.sqlite
```

## Create a root user

```sh
$ python manage.py createsuperuser
```

## To run tests and export coverage
```sh
$ pip install -r requirements/local.txt
$ pytest --cov-report term-missing --cov-report html -s
```

To see the coverage on your browser: 
```sh
$ open htmlcov/index.html
```

## To get a bearer token
* Method: POST

```sh
$ curl --request POST \
  --url http://localhost:8000/api/v1/token/ \
  --header 'Content-Type: application/json' \
  --data '{"email": "youruseremail@gmail.com", "password": "yourpassword"}'
```

## File api

By default, our application url will be running at localhost:8000 and our api default url is ```/api/v1```
The file's api path is ```/api/v1/files/```

### To create a file

* Method: POST

```sh
$ curl --request POST \
  --url http://localhost:8000/api/v1/files/ \
  --header 'Authorization: Bearer {your_bearer_token}' \
  --header 'Content-Type: multipart/form-data' \
  --form 'file=@/Users/path/to/your_file.png' \
  --form folder={optional_folder_id}
```

### To retrieve a file
* Method: GET
```sh
$ curl --request GET \
  --url 'http://localhost:8000/api/v1/files/?folder={folder_id_optional}' \
  --header 'Authorization: Bearer {your_bearer_token}'
```

## Folder api

### To create a folder

* Method: POST

```sh
$ curl --request POST \
  --url http://localhost:8000/api/v1/folders/ \
  --header 'Authorization: Bearer {your_bearer_token}' \
  --header 'Content-Type: application/json' \
  --data '{"name": "2", "parent_folder": "{optional_folder_id_to_insert_into_it}"}'
```

### To retrieve a folder

* Method: GET
```sh
$ curl --request GET \
  --url http://localhost:8000/api/v1/folders/{folder_id} \
  --header 'Authorization: Bearer {your_bearer_token}'
```


### To list the folders

* Method: GET
```sh
$ curl --request GET \
  --url http://localhost:8000/api/v1/folders/ \
  --header 'Authorization: Bearer {your_bearer_token}'
```

## Directories api

```sh
$ curl --request GET \
  --url 'http://localhost:8000/api/v1/directories/?folder={folder_id_or_leave_blank_for_root}' \
  --header 'Authorization: Bearer {your_bearer_token}'
```
