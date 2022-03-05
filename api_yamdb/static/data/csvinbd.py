import csv
import sqlite3

# путь к файлу может отличаться. r чтобы символы не экранировались
connection = sqlite3.connect(r'C:\Dev\api_yamdb\api_yamdb\db.sqlite3')
cursor = connection.cursor()

with open(
        'category.csv', 'r', newline='', encoding='utf-8'
) as csvfile:
    reader_category = csv.DictReader(csvfile, delimiter=',')
    to_db_category = [
        (row['id'], row['name'], row['slug'], '')
        for row in reader_category
    ]

with open('genre.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader_genre = csv.DictReader(csvfile, delimiter=',')
    to_db_genre = [
        (row['id'], row['name'], row['slug'], '')
        for row in reader_genre
    ]

with open(
        'titles.csv', 'r', newline='', encoding='utf-8'
) as csvfile:
    reader_titles = csv.DictReader(csvfile, delimiter=',')
    to_db_titles = [
        (row['id'], row['name'], row['year'], row['category'])
        for row in reader_titles
    ]

with open(
        'genre_title.csv', 'r', newline='', encoding='utf-8'
) as csvfile:
    reader_genre_title = csv.DictReader(csvfile, delimiter=',')
    to_db_genre_title = [
        (row['id'], row['genre_id'], row['title_id'])
        for row in reader_genre_title
    ]

with open(
        'review.csv', 'r', newline='', encoding='utf-8'
) as csvfile:
    reader_review = csv.DictReader(csvfile, delimiter=',')
    to_db_review = [
        (row['id'], row['text'], row['pub_date'],
         row['author'], row['title_id'], row['score'])
        for row in reader_review
    ]

with open(
        'comments.csv', 'r', newline='', encoding='utf-8'
) as csvfile:
    reader_comments = csv.DictReader(csvfile, delimiter=',')
    to_db_comments = [
        (row['id'], row['text'], row['pub_date'],
         row['author'], row['review_id'])
        for row in reader_comments
    ]

with open(
        'users.csv', 'r', newline='', encoding='utf-8'
) as csvfile:
    reader_users = csv.DictReader(csvfile, delimiter=',')
    to_db_users = [
        (row['id'], '', '', '', row['username'],
         row['first_name'], row['last_name'],
         row['email'], '', '', '', row['bio'], row['role'])
        for row in reader_users
    ]

cursor.executemany(
    "INSERT INTO reviews_category "
    "(id, name, slug, description) VALUES (?, ?, ?, ?)",
    to_db_category
)
connection.commit()
cursor.executemany(
    "INSERT INTO reviews_genre (id, name, slug, description)"
    " VALUES (?, ?, ?, ?)",
    to_db_genre
)
connection.commit()
cursor.executemany(
    "INSERT INTO reviews_titles (id, name, year, category_id)"
    " VALUES (?, ?, ?, ?)",
    to_db_titles
)
connection.commit()
cursor.executemany(
    "INSERT INTO reviews_genre_title (id, genre_id, title_id)"
    " VALUES (?, ?, ?)",
    to_db_genre_title
)
connection.commit()
cursor.executemany(
    "INSERT INTO reviews_review (id, text, pub_date, author_id, title_id, score)"
    " VALUES (?, ?, ?, ?, ?, ?)",
    to_db_review
)
connection.commit()
cursor.executemany(
    "INSERT INTO reviews_comments (id, text, pub_date, author_id, review_id)"
    " VALUES (?, ?, ?, ?, ?)",
    to_db_comments
)
connection.commit()
cursor.executemany(
    "INSERT INTO users_user (id, password, last_login, is_superuser,"
    " username, first_name, last_name, email, is_staff, is_active, "
    "date_joined, bio, role)"
    " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    to_db_users
)
connection.commit()
connection.close()