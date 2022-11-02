# Test_task

В реализации проекта API Registration-Login использована БД PostgreSQL

Для работы необходима установка PostgreSQL и DjangoREST Framework, а также модуля psycopg2, для работы с базой.

В конфиге БД (файл settings.py) необходимо заменить символы * на значения пользователя: имя базы, к которой осуществляется подключение, 
имя пользователя и пароль. 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '******',
        'USER': '******',
        'PASSWORD': '******',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
