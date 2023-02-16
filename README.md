###### Итоговый учебный проект курса QAP ([Skillfactory](https://lms.skillfactory.ru/courses/course-v1:SkillFactory+INTQAP+2022/course/))
### Тестирование нового интерфейса страницы авторизации Ростелеком.  

В проекте применялись следующие инструменты:
- сервис временной почты [tempmail+](https://tempmail.plus) для авторизации;
- сервис [Random string generator](http://www.unit-conversion.info/texttools/random-string-generator/) для генерации тестовых данных;
- техники граничных значений и классы эквивалентности для оптимизации тестовых данных;
- паттерн PageObject в связке с фреймворками [pytest](https://docs.pytest.org) и [selenium](https://www.selenium.dev);
- библиотека [Smart Page Object](https://github.com/TimurNurlygayanov/ui-tests-example.git);
- Chrome DevTools для анализа страниц и формирования локаторов;
- pytest-фикустура `parametrize` для тестирования полей ввода в формах;
- pytest-фикустура `xfail` для маркировки возможного падения тестов;

Тест-кейсы и баг-репорты доступны [здесь](https://docs.google.com/spreadsheets/d/1dfNgr6-cX_geA6LvlG2y_jLam04xc_eFkFhX736RJnA/edit?usp=share_link).
***
**Структура проекта:**
+ pages/ - PageObject-модели страниц
+ tests/ - файлы тестов
+ settings.py - данные для тестирования

**Для запуска тестов:**
1. склонировать репозиторий
1. установить [poetry](https://python-poetry.org/)
2. в директории проекта выполнить комманду `poetry install`
3. запуск тестов `poetry run pytest -v`
***
TODO: Пока не разобрался как использовать ids в выводе при использовании параметризации (объект request).
