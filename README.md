# Diplom_3
Автотесты UI для [Stellar Burgers](https://qa-stellarburgers.education-services.ru/).
Python, Selenium, pytest, Allure. Тесты запускаются в Chrome и Firefox.

## Структура

- `api/` — клиенты API (создание и удаление тестового пользователя)
- `config/` — настройки (адрес стенда, таймаут)
- `data/` — пути страниц и API, модели данных
- `helpers/` — запуск браузеров, генерация данных
- `locators/` — локаторы элементов страниц
- `pages/` — Page Object
- `tests/` — тесты и фикстуры
- `allure-report/` — собранный отчёт Allure

## Установка

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск тестов

```bash
python -m pytest              # браузеры с окнами
python -m pytest --headless   # без окон
```

Адрес стенда и таймаут можно задать переменными окружения `BASE_URL` и `TIMEOUT`.

## Allure-отчёт

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```