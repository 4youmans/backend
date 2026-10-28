# Отчёт кафе

Студент: Паюсов Семён, группа РПО 2\25.

Программа читает `data/smena.csv`, нормализует имена официантов,
считает выручку по каждому и выводит общий итог `4 937,50 ₽`.
В функциях и переменных добавлены аннотации типов.

## Запуск в Windows PowerShell

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe main.py
```

При отсутствии Python 3.12 укажите путь к установленному Python этой версии.
Окружение `.venv` создаётся локально и не входит в репозиторий.

## Проверки

```powershell
.venv\Scripts\python.exe -m mypy app
.venv\Scripts\python.exe -m pytest -q
```

Ожидаемый результат: mypy без ошибок и 12 пройденных тестов.
Настройки VS Code сохранены в `.vscode/settings.json`, режим `basic`.
Расширения Python и Pylance нужно проверить в самом редакторе.
