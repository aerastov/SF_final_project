#ЗАДАЧИ

Перед вами стоят следующие задачи:

###SPRINT 1
1. Создание репозитория.
Для начала вам нужно создать репозиторий на GitHub, Bitbucket или другом VCS-ресурсе. Если во время прохождения курса 
вы ещё не создали аккаунт ни на одном из этих ресурсов, сейчас самое время для этого! В репозитории, который вы создаёте, 
будет храниться весь ваш код, а также, возможно, настройки Continuous Integration, о которых мы подробнее поговорим в 
следующих спринтах. Кроме того, вы сможете попрактиковаться в написании красивых коммит-месседжей, чтобы менторам было 
понятнее, как у вас шла работа. ;)
2. Создание проекта для бэкенд-приложения.
Мы рекомендуем вам использовать Django и сразу подключить django-rest-framework, так как именно эти технологии мы изучали 
на курсе, и именно по ним наши менторы смогут вам лучше всего помочь, однако вы не ограничены в выборе технологий!
3. Первоначальная настройка проекта.
Если вы всё-таки решите использовать Django, особое внимание рекомендуем уделить настройке MEDIA_ROOT, которая отвечает 
непосредственно за хранение медиафайлов. Его можно организовать просто в отдельной папке на сервере, однако, в качестве 
«задачи со звездочкой» мы рекомендуем вам настроить использование библиотеки django-storages для хранения файлов на AWS S3. 
4. Подключение базы данных.
Мы настоятельно рекомендуем использовать Postgres, использование которого с Django подробно разобрано в курсе, однако, 
как и во всех решениях в этом проекте, мы не ограничиваем вас в выборе. 
5. Подключение инструментов для аутентификации и регистрации.
Мы рекомендуем использовать auth0 или другой похожий инструмент, позволяющий пользователям заходить в ваше приложение 
через аккаунты сторонних провайдеров.

###SPRINT 2
Дизайн структуры базы данных.

1. Вам необходимо расписать сущности и связи между ними в виде отдельного документа, который мы рекомендуем поддерживать 
в актуальном состоянии в ходе внесения изменений в проект — вам так будет легче жить. :)

На этом этапе нужно хорошо продумать, какой функционал у приложения и какие требования это создаёт к структуре базы 
данных. Мы не рекомендуем посвящать время планированию сущностей чатов и сообщений, так как на них отведено отдельное 
время позднее, при настройке WebSocket-чата.

Рекомендуется особенно внимательно подумать о следующих сущностях и связях между ними:
- Пользователь; 
- Видеоролик;  
- Комментарий; 
- Подписка; 
- Бан/игнор; 
- Лайк.

2. Перенос созданной концепции в форму кода.

На этом этапе вы создадите непосредственно код моделей. Мы рекомендуем особенно внимательно продумать, какие именно 
между сущностями связи: например, где лучше использовать FK-связи, а где — MTM. Рекомендуется также написание 
автоматических тестов на функционал моделей.

3. Создание миграций и их прогон на поднятой базе данных.

На этом этапе вам необходимо убедиться, что миграции, во-первых, корректно генерируются, во-вторых, проходят без ошибок,
и в-третьих, создают корректные структуры в базе данных. Для проверки последнего рекомендуется использовать интерфейс 
взаимодействия с БД напрямую, например, через CLI.

4. Подключение поиска к моделям.

Рекомендуется реализация отдельного метода на моделях, по которым нужен поиск, но вы также можете воспользоваться 
сторонними библиотеками для поиска, которых существует огромное количество.


##Примечания к проекту:
## В проекте применены:
- Рабочая среда Docker-compose
- Django 4.1.1
- Библиотека авторизации django-allauth
- API djangorestframework
- БД Postgres 14
- Хранение медиафайлов организовано в отдельных папках на сервере, так как зарегистрировать из России AWS S3 на
данный момент не представляется возможным. 
- Создана модель пользователя через расширение AbstractBaseUser для добавления новых полей и регистрации по e-mail
- Возможность получения данных для регистрации через аккаунт google (OAuth2) используя frontend приложение (react). 
Frontend обращается к api google и получает access_token, далее передает его на api django, который, используя
access_token получает от api google e-mail, name, surname и ссылку на фото пользователя.
- Созданы необходимые модели и связи между их полями.
- Все манипуляции с данными в backend планируется осуществлять через react с помощью rest api



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

После завершения установки и запуска контейнеров:

###Backend Django: войти на страницу администрирования:  
http://localhost:8000/admin  
логин: admin@mail.ru  
пароль: admin

###Frontend:
Frontend в docker compose временно не добавлен.  
Если еще не установлен nodejs, то установить с офсайта:  
https://nodejs.org/en/download/  
В консоли перейти в папку Frontend, восстановить модули:  
`npm install`  
После завершения установки, набрать:  
`npm start`  
Страница будет доступна по адресу:  
http://localhost:3000




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
pip install django-cors-headers //для обработки запросов с разных доменов
pip install psycopg2-binary
pip install requests
pip install django-phonenumber-field[phonenumbers]
pip install Pillow //для работы с ImageField

-->