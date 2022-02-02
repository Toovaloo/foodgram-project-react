# foodgram

Дипломный проект курса Python-разработчик на Яндекс.Практикум.

![foodgram workflow](https://github.com/bayborodin/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

## Описание проекта

С помощью сервиса **foodgram** (продуктовый помощник) пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Запуск проекта
Для запуска проекта необходимо из директории `/infra` выполнить команду:
```
docker-compose up
```

Далее необходимо сделать миграции базы данных и собрать статику:

```
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py collectstatic --no-input 
```
Создание суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

API доступно по IP-адресу http://62.84.124.60/api/

(email: admin@mail.ru, password: admin)