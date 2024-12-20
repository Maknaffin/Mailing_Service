# Mailing_Service

## Описание
**Mailing_Service** — это веб-приложение для управления рассылками электронных писем. Оно позволяет пользователям легко создавать, планировать и отправлять массовые электронные письма с помощью простого интерфейса.

## Используемые технологии
- **Django** — основной фреймворк для разработки веб-приложения.
- **PostgreSQL** — реляционная база данных для хранения информации о пользователях и рассылках.
- **Redis** — система управления базами данных в памяти, используемая для кэширования и очередей задач.
- **django-apscheduler** — библиотека для планирования задач в Django.
- **Docker** — контейнеризация приложения для упрощения развертывания и управления зависимостями.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Maknaffin/Mailing_Service.git
   cd Mailing_Service
   
2. Убедитесь, что у вас установлен Docker и Docker Compose.
3. Создайте файл .env на основе .env.example и настройте переменные окружения.
4. Запустите контейнеры:
    ```bash
    docker-compose up --build
5. После запуска контейнеров выполните миграции базы данных:
    ```bash
    docker-compose exec app python manage.py migrate
6. Создайте суперпользователя для админ-панели:
    ```bash
   docker-compose exec app python manage.py csu
7. Перейдите по адресу http://localhost:8000/ в вашем браузере.

## Использование

- После входа в систему вы сможете создавать новые шаблоны писем и добавлять получателей.
- Используйте интерфейс для планирования рассылок на определенное время.
- Отслеживайте статус отправленных писем через админ-панель.

## Лицензия

Этот проект лицензирован под MIT License - смотрите файл LICENSE для подробностей.