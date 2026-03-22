# Daily-planner

## Структура БД
База данных содержит одну таблицу: tasks

```id``` - id задачи в таблице

```title``` - название задачи

```description``` - описание задачи

```status``` - статус задачи, имеет три варианта: STARTED, PROCESSED, FINISHED

## Запуск приложения

### Через docker (Linux)
На текущей машине должны быть установлены docker и docker-compose. Вам необходимо склонировать данный репозиторий и перейти в папку Daily-planner

```git clone git@github.com:Danila-gi/Daily-planner.git```

```cd Daily-planner```

Создать файл .env (скопировать данные из .env.examplae)

```cp .env.example .env```

Создаются образы: образ для БД, образ backend приложения

```docker-compose build```

Приложение запускается

```docker-compose up```

После этого сервер будет доступен по адресу http://localhost:8000/, а база данных - http://localhost:5433/. Все API запросы дальнейшие прописываются на адрес сервера.

### API документация

Добавить задачу: ```POST /add-task/```

Удалить задачу: ```DELETE /delete-task/```

Изменить данные задачи: ```PUT /update-task/```

Получить все задачи: ```GET /get-all-tasks/```

Получить информацию о конкретной задаче: ```GET /get-task?title={title}```

### Пример запросов

```bash
# Добавление задач
curl -X POST "http://localhost:8000/add-task"   -H "Content-Type: application/json"   -d '{
    "title": "Задача 1",
    "description": "сделать задачу 1",
    "status": "started"
  }'

curl -X POST "http://localhost:8000/add-task"   -H "Content-Type: application/json"   -d '{
    "title": "Задача 2",
    "description": "сделать задачу 2",
    "status": "started"
  }'
  
curl -X POST "http://localhost:8000/add-task"   -H "Content-Type: application/json"   -d '{
    "title": "Задача 3",
    "description": "сделать задачу 3",
    "status": "started"
  }'
  
# Получение данных конкретной задачи
curl -G "http://localhost:8000/get-task" --data-urlencode "title=Задача 1"

# Получение данных всех задач
curl -G "http://localhost:8000/get-all-tasks"

# Изменить данные задачи
curl -X PUT "http://localhost:8000/update-task"   -H "Content-Type: application/json"   -d '{
    "title": "Задача 3",
    "description": "сделать задачу 3",
    "status": "finished"
  }'
  
# Удалить задачу
curl -X DELETE "http://localhost:8000/delete-task"   -H "Content-Type: application/json"   -d '{
    "title": "Задача 2"
  }'

```
