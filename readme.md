## Итоговый проект. ТЗ

Итоговый проект включает в себя разработку бэкенд- и фронтенд-частей веб-приложения социальной сети, ориентированной на 
видеоконтент.  
С функциональной стороны он должен включать в себя такие возможности:

- поиск и просмотр загруженных пользователями видеороликов; 
- регистрация и авторизация пользователей; 
- добавление и управление видеороликами зарегистрированными пользователями; 
- связи пользователей друг с другом через чаты (ЛС и групповые); 
- рассылка уведомлений по разным каналам связи.

Далее подробнее про каждую из частей функционала.  

1. Просмотр видео.
У пользователей есть две ленты с видео: «Подписки» и «Для вас». Так как компетенции по Machine Learning в наш курс не 
входят, лента «Для вас» будет формироваться просто по принципу «показать самые последние загруженные видео». 
2. Поиск видео.
У пользователя есть возможность поиска по видео: как по хэштэгам, так и по тексту в описании и комментариях. 
3. Регистрация и авторизация.
Регистрация должна осуществляться через стороннюю учетную запись, например, Google (рекомендованная система 
аутентификации: auth0.com). E-mail, юзернейм и номер телефона должны быть обязательными полями для заполнения в профиле. 
4. Управление видео.
Создание, редактирование, архивирование, полное удаление – все эти действия может выполнить автор видео. Чужие видео 
можно только смотреть.
Следует отдельно отметить, что создание какого-либо видеоредактора для данного проекта не требуется; пользователи просто 
должны иметь возможность загружать видеофайлы. 
5. Связь с другими пользователями.
Со страницы видео с помощью нажатия на аватар автора пользователь должен иметь возможность открыть профиль автора и 
перейти в веб-чат с ним, который работает, используя технологию WebSockets или socket.io. После отправки сообщения 
пользователю, если оно не прочитано в течение суток, ему должен быть отправлен e-mail о непрочитанном сообщении. 
6. Уведомления
Уведомления пользователям должны осуществляться через:
- Web Push (например, с помощью Django-Webpush); 
- Email; 
- для подтверждения номера телефона должен использоваться канал смс (Twilio или другой сервис).  


## В проекте применены:
- Рабочая среда Docker-compose
- Django 4.1.1
- Библиотека авторизации django-allauth
- API djangorestframework
- БД Postgres 14
* Хранение медиафайлов организовано в отдельных папках на сервере, так как зарегистрировать из России AWS S3 на
данный момент не представляется возможным. 



## Установка docker
Для lunix систем:   
```curl -fsSL https://get.docker.com/ | sh``` //Установка Docker  
Для Windows или Macos:  
```https://www.docker.com/``` //Установка Docker Desktop  

## Запуск приложения:  
После установки docker, загружаем проект командой:  
`git clone https://github.com/aerastov/SF_final_project.git`  
В командной строке, переходим в директорию проекта и набираем:  
`sudo docker-compose up -d`  //В среде lunix
`docker-compose up -d` //Docker Desktop (Windows или Macos)
После завершения установки и запуска контейнеров, заходим в браузере по адресу:  
(в случае не запуска какого-либо контейнера, запустить его в ручную)
http://localhost:8000  
Войти на страницу администрирования можно по адресу:  
http://localhost:8000/admin  
логин: admin  
пароль: admin



Автор проекта: **Ерастов Алексей Сергеевич**  
e-mail: a.erastov@gmail.com  
Группа SkillFactory: FPW-36  
Москва, сентябрь 2022г.

















<!--
python manage.py createsuperuser
venv\Scripts\activate
python manage.py startapp myapp
pip freeze > requirements.txt
python -m pip install --upgrade pip
python manage.py runserver

pip install django
pip install djangorestframework
python -m pip install django-cors-headers
pip install psycopg2-binary

-->