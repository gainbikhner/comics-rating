# comics-rating

На сайте комиксов реализована система оценки и отображения рейтинга для каждого комикса. Рейтинг основан на средней оценке, которую пользователи могут ставить комиксам от 1 до 5. Рейтинг обновляемым в реальном времени. 

## Автор

https://github.com/gainbikhner

## Стек технологий

- Python 3.9.10
- Django 4.2.8

## Инструкция

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:gainbikhner/comics-rating.git
cd comics-rating
```

2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
source venv/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:

```
pip install --upgrade pip
pip install -r requirements.txt
```

4. Сделать и выполнить миграции:

```
cd comics_rating
python3 manage.py makemigrations
python3 manage.py migrate
```

5. Создать файл .env и добавить в него секретный ключ.

6. Запустить проект:

```
python3 manage.py runserver
```

## Тесты

Чтобы запустить тесты выполните команду:

```
python3 manage.py test
```

## Endpoints

Создание оценки комикса:

```
POST http://localhost/api/ratings/

{
  "comic_id": int,
  "user_id": int,
  "VALUE": int,
}
```

Получение рейтинга конкретного комикса:

```
GET http://localhost/api/comics/<comic_id>/rating/
```