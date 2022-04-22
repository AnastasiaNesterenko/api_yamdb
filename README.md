# Проект YaMDb

## Учебный проект на подобии IMDb

### Описание

В данном проекте реализованы функции выставления оценок на произведения,
написание рецензий, написание комментариев к рецензиям.

### Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AnastasiaNesterenko/api_yamdb.git
```

Cоздать и активировать виртуальное окружение:
```
python -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:
```
python3 manage.py migrate
```

Запустить скрипт для заполнения БД данными.
Файл расположен \api_yamdb\static\data\csvinbd.py
```
ПКМ -> Run csvinbd
```

Запустить проект:
```
python manage.py runserver
```
