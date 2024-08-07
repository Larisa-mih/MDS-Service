<h3 align="center">Сайт компании медицинской диагностики</h3>


## О проекте

# Тема проекта: BF2 Fullstack

# Сайт компании медицинской диагностики "MDS-Service"

Данный проект представляет собой веб-приложение сайта компании медицинской диагностики.

## Стек. Использованные технологии

- Python
- PostgreSQL (для хранения и обработки данных в реализованном проекте)
- ORM
- Django (фреймворк для реализации)
- Templates (работа с построением шаблонов и шаблонизаторами)
- Forms (для реализации интерфейсов заполнения или редактирования данных)
- Auth (функционал авторизации)
- Git (для хранения исходного кода)
- Readme (документацию/инструкция)

## Функционал и возможности

- Регистрация и авторизация пользователей
- Создание, просмотр, редактирование и удаление записей на приём/УЗИ/ЭКГ/Анализы
- Просмотр всех врачей-специалистов клиники
- Просмотр таблиц-прайсов всех услуг клиники (УЗИ, ЭКГ, Анализы)
- Регистрация и верификация пользователей через отправку подтверждающего письма на email

## Настройка проекта

Для работы с проектом произведите базовые настройки.

### 1. Клонирование проекта

Клонируйте репозиторий используя следующую команду.
  ```
  git clone https://github.com/Larisa-mih/MDS-Service.git
  ```

### 2. Настройка виртуального окружения и установка зависимостей

Создает виртуальное окружение:
```text
python3 -m venv venv
```

Активирует виртуальное окружение:
```text
source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate.bat         # для Windows
```

Устанавливает зависимости:
```text
pip install -r requirements.txt
```

### 3. Создайте 2 файла по шаблону `.env_sample` назовите их `.env.local и .env.docker` и заполните необходимые переменные окружения
```text
# Django
SECRET_KEY=secret_key - секретный ключ django проекта

# PostgreSQL
POSTGRES_DB="db_name" - название вашей БД
POSTGRES_USER="postgres" - имя пользователя БД
POSTGRES_PASSWORD="secret" - пароль пользователя БД
POSTGRES_HOST="host" - для .env.local 127.0.0.1 для .env.docker db
POSTGRES_PORT=5432 - port

# Mailing  
EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_HOST_USER='your_email@yandex.ru' - ваш email yandex
EMAIL_HOST_PASSWORD='your_yandex_smtp_password' - ваш пароль smtp yandex
```

### 4. Подключение к базе данных
Вам нужно установить PosgreSQL. 
```
https://www.postgresql.org/download/
```

Затем создать Database.
```
CREATE DATABASE name_database;
```
### 5. Для локального запуска:

#### 5.1 Применить миграции:
```
python manage.py migrate
```

#### 5.2 Для создания суперюзера используйте команду
    * python manage.py csu
    * Административная панель доступна по адресу: http://127.0.0.1:8000/admin/

   
#### 5.3 Запустите сервер:
    * python manage.py runserver

### 6. Для развертывания проекта через Docker:

- установите Docker себе в систему, перейдя по [ссылке](https://docs.docker.com/engine/install/)
- для сборки проекта и запуска введите команду:

```text
docker-compose up -d --build
```

Ссылка на репозиторий: [https://github.com/Larisa-mih](https://github.com/Larisa-mih)