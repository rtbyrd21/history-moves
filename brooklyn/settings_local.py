import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_0639161351e83ae',
        'USER': 'bf2906c2b0cbc2',
        'PASSWORD': '86c85ba9',
        'HOST': 'us-cdbr-iron-east-04.cleardb.net',
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }