from reflex_report.components.code_block import code_block
from reflex_report.components.menu_item import menu_item
from ...template.base import template
import reflex as rx

from .example_parrot_facts import index as e1


@rx.page(route="/start", title="🚀" * 5)
@template
def index():
    return rx.vstack(
        rx.markdown("# Начинаем"),
        rx.markdown("Как вы уже заметили сам доклад полностью написан с помощью `reflex`. Было бы сложно сделать его в `Jupyter Notebook` (сложно запускать), а в `Markdown` слишком скучно. Хочется динамики! Давайте на что нибудь посмотрим: "),
        rx.markdown("## Пример"),
        rx.markdown("Давайте для начала посмотрим на какой нибудь простенький пример использования `reflex`"),
        e1,
        code_block("reflex_report/pages/start/example_parrot_facts.py"),
        rx.markdown(
            "В этом коде есть три основные части.\n\n"
            "Где тут пользовательский интерфейс?\n\n"
            "`Frontend` описывается в функции `index`. Она возвращает объект типа `rx.Component`. Весь пользовательский интерфейс в `reflex` описывается декларативно используя компоненты `reflex`'а. Например этот текст `rx.markdown`. В компоненты можно передавать разные аргументы, стили, состояния, другие компоненты и так далее. Так же можно делать свои собственные компоненты, каковым является `index`.\n\n"
            "А где серверная логика?\n\n"
            "`Backend` тут описан выше в классе `State`. На всё, что написано в классе наследуемом от `rx.State`, можно ссылаться из `frontend` (переменные и методы). Код будет выполняться прямо на сервере, так что тут можно использовать `python` библиотеки, подключаться к БД и так далее.\n\n"
            "Как добавить такой код на какую-то страницу?\n\n"
            "За `роутинг` отвечает последние две строчки. Там создаётся приложение и с помощью метода `add_page` добавляется компонент в качестве страницы. Как ещё можно добавлять страницы и какие извращения с компонентами можно творить посмотрим позже. Эта часть призвана заинтерисовать."    
        ),
        rx.flex(
            menu_item("В воду зашли. Учимся плавать", "arrow-right", "/basics"),
            style={
                "width": "100%",
            },
            justify="end",
        ),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        rx.markdown(""),
        style={
            "width": "100%",
        },
    )
