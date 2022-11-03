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

После установки необходимых модулей и подключения к базе, вводом команды python manage.py migrate создаётся таблица в указанной вами базе,
с названием "Registration_Login_user". Эта команда сама создаст необходимую таблицу, SQL применяется только для извлечения данных из базы.

Запускаем сервер (python manage.py runserver), и можно тестировать запросы. По ссылкам v1/auth/register и v1/auth/login доступны html-формы 
дженериков DjangoREST. Также возможно тестирование с помощью Postman.

