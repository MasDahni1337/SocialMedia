# Social Media With Django

Set your database and time zome in `SimpleGuna/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SimpleGuna', #change this with your name database
        'USER': 'zeromind', #change this with your user database
        'PASSWORD' : '1', # change this with your password database
        'HOST' : '127.0.0.1',
        'PORT': '3306',
    }
}


TIME_ZONE = 'Asia/Jakarta' #change with your time zone

```

## Screenshoot / Demo
### Login page
<img src="ss/login.png">

### Register Page
<img src="ss/regis.png">

### Home page
<img src="ss/home-page.png">
<img src="ss/home-page-2.png">

### Comment
<img src="ss/comment.png">

if you want to work together and help develop this social media, just pull request
