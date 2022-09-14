from email.charset import BASE64
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbprueba_mysql',
        'USER': 'root',
        'PASSWORD': '56809',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}