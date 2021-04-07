set FLASK_APP=webapp && flask db migrate -m "Полю наме таблицы user добавлено свойство уникальности"
flask db upgrade