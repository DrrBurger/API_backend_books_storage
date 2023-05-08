# API_backend_books_storage
- Бекенд приложение на python с использованием Django и базой данных SQLite,
которое предоставляет API для работы с объектами "Книга" и "Автор".
- Для доступа к эндпойнтам будет использоваться токен-аутентификация.
- Добовлять записи в БД могут только авторизованые пользователи
- Изменять запись может только тот кто её добавил или администратор
- Удалять записи может только администратор
---
- В связи с этим реализована следующая логика:
- При создании обьекта 'Автор' в качестве создателя обьекта(не автора книги! не путать!) ему автоматически присваивается текущий авторизованый пользователь.
- При создании обьекта 'Книга' вы можете выбрать автора книги из базы данных и так же автоматически привязывается создатель обьекта (текущий авторизованый пользователь).
