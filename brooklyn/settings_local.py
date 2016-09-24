import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_c0e83815b3d04bd',
        'USER': 'bcf89b7f8352b0',
        'PASSWORD': 'cfc369ac',
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