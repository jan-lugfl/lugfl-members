# lugfl-members

This is a Django project meant to maintain Association members


## Setup your local development Environment


Copy lugflmembers/local_settings.py.dist to lugflmembers/local_settings.py

```bash
cp lugflmembers/local_settings.py.dist lugflmembers/local_settings.py
```

Change your Settings for your local Database in `lugflmembers/local_settings.py`.

Set `DJANGO_SETTINGS_MODULE` to the local_settings module:

```bash
export DJANGO_SETTINGS_MODULE=lugflmembers.local_settings
```

Create your database schema or update it to the current version:

```bash
python manage.py migrate
```


Create a superuser to login into your admin interface:

```bash
python manage.py createsuperuser
```


Run the Test-Server:

```bash
python manage.py runserver
```

Go to your Admin-Interface: http://localhost:8000/admin/


