from reflex_report.components.code_block import code_block
from reflex_report.components.menu_item import menu_item
from ...template.base import template
import reflex as rx


@rx.page(route="/installation", title="🤔" * 5)
@template
def index():
    return rx.vstack(
        rx.markdown(
            "# Установка и Запуск\n"
            "## Создаём проект\n"
            "`Reflex` это полноценный фреймфорк, по этому для работы с ним нужно создавать отдельный проект:"
        ),
        rx.code_block(
            "mkdir my_app\ncd my_app",
            can_copy=True,
        ),
        rx.markdown(
            "## Создаём виртуальную среду"
        ),
        rx.code_block(
            "python -m venv venv\n./venv/Scripts/activate",
            can_copy=True,
        ),
        rx.markdown(
            "или"
        ),
        rx.code_block(
            "python -m venv venv\nsource ./venv/bin/activate",
            can_copy=True,
        ),
        rx.markdown(
            "## Устанавливаем пакет"
        ),
        rx.code_block(
            "pip install reflex",
            can_copy=True,
        ),
        rx.markdown(
            "## Инициализация проекта\n"
            "Для инициализации проекта существует консольная команда `reflex init`. Можно установить имя проекта (`--name`), можно использовать обширную библиотеку шаблонов (`--template` (шаблоны можно посмотреть на их сайте)), можно утсановить уровень логов (`--logLevel`), так же у них появилась фича Генерация шаблона с помощью ИИ (`--ai`)\n"
            "Но не будем замарачиваться и просто инициализируем пустое приложение:"
        ),
        rx.code_block(
            "reflex init",
            can_copy=True,
        ),
        rx.markdown(
            "## Запустим приложегние\n"
            "Запустим приложение в dev моде:"),
        rx.code_block(
            "reflex run",
            can_copy=True,
        ),
        rx.markdown(
            "Теперь приложение запущено (обычно `frontend` на `http://localhost:3000`, а `backend` `http://localhost:8000`). Оно будем перезапускаться при любых изменениях файлов проекта."
        ),
        rx.flex(
            menu_item("Облились водой. Теперь заходим в воду", "arrow-right", "/start"),
            style={
                "width": "100%",
            },
            justify="end",
        ),
        style={
            "width": "100%",
        },
    )
    
