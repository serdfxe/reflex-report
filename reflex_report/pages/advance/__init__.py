from reflex_report.components.code_block import code_block
from reflex_report.components.menu_item import menu_item
from ...template.base import template
import reflex as rx

@rx.page(route="/advance", title="🦾" * 5)
@template
def index():
    return rx.vstack(
        rx.markdown("# Не база"),
        rx.markdown("## Структура проекта"),
        rx.markdown("Мы рассмотрели все базовые и не только инструменты для создания компонентов и регистрации страниц. Как вообще выглядит `reflex` приложение?"),
        rx.markdown("Файловая структура `reflex` приложения следующая:"),
        code_block("",
"""
my-app
├── .web
├── assets
├── my-app
│   ├── __init__.py
│   └── my_app.py
└── rxconfig.py
"""
        ),
        rx.markdown("В директории `.web` происходит вся магия создания `frontend` по нашему коду на `python`. Там храниться сгенерированный `js` код. Трогать её нет необходимости, но я рекомендую посмотреть что вообще там происходит."),
        rx.markdown("Например в ней есть директория `.web/pages`, в которой храняться все скомпилированные страницы приложения."),
        rx.markdown("При инициализации проекта создаётся папка с таким же именем. В ней как раз таки можно работать. (в примере выше `my-app/`). В этой директории находиться файл с дефолтным приложением."),
        rx.markdown("В директории `assets` можно хранить публично доступные файлы, такие как изображения, щрифты и так далее. К ним можно обращаться следующим образом (`assets/parrot.png`):"),
        code_block("", 
"""
rx.image(src="parrot.png")
"""
        ),
        rx.markdown("Папка `assets` подходит только для статических файлов. Если вдруг в вашем приложении есть логика связанная с динамическим предоставлением файлов, то для этого подойдёт директория `/uploaded_files` (можно поменять с помощью переменной окружениыя `REFLEX_UPLOADED_FILES_DIR`). Чтобы получить директорию в коде можно воспользоваться `rx.get_upload_dir()`, а чтобы создать ссылку `rx.get_upload_url(relative_path)`. Получить к ним доступ можно через бэкенд (обычно запускается на порту `8000`) по ссылке `/_upload/<path>`"),
        rx.markdown("## Конфигурация"),
        rx.markdown("Чтобы настроить наше приложение нужно поменять конфигурацию в файле `rxconfig.py`, которая находится в корне проекта. Изначально конфиг выглядит так:"),
        code_block("",
"""
import reflex as rx

config = rx.Config(
    app_name="my_app",
)
"""
        ),
        rx.markdown("В `rx.Config` можно передать следующие аргументы: `app_name`, `loglevel`, `frontend_port`, `backend_port`, `frontend_path`, `api_url`, `env_file`. Это основные."),
        rx.markdown("Так же можно держать конфигурацию в `.env` файле и обновлять через метод `update_from_env`"),
        rx.markdown("## Что у `Reflex` под капотом?"),
        rx.markdown("Неожиданно, но у приложения `reflex` 2 части: `frontend` (на `React`) и `backend` (на `FastAPI`)."),
        rx.markdown("Так как в `python` нет хороших расширений синтаксиса для написания HTML шаблонов, как jsx, (единственный, который я знаю (`packed`) последний раз обновлялся 9 лет назад 😭, надеюсь ещё появиться хороший инструмент) `Reflex` строит компоненты с помощью `python` функций. Происходит это примерно так:"),
        code_block("",
"""
def index():
    return rx.vstack(
        rx.image(
            src=ParrotState.url,
        ),
        rx.text(
            "Parrot!",
        ),
        rx.button(
            "next",
            on_click=ParrotState.next,
        ),
    )
"""
        ),
        code_block("",
"""
<VStack>
    <Image src={ParrotState.url}/>
    <Text>
        Parrot!
    </Text>
    <Button onClick={ParrotState.next}>
        next
    </Button>
</VStack>
"""
        ),
        rx.markdown("`Reflex` использует библиотеку UI компонентов `Radix`, а для работы с адаптивными `css` стилями библиотеку `Emotion`."),
        rx.markdown("Кроме самого интерфейса в `frontend` части есть ещё 2 сущности: `триггеры` событий и `очередь` событий. `Триггеры` - это те события, на которые повешаны обработчики, например `on_blur=MyState.set_text`. Когда происходит событие и `триггер` вызывается, он помещает в `очередь` событий следующую информацию:"),
        code_block("", 
"""
{
    client_token: "...token...",
    event_handler: "MyState.set_text",
    arguments: ["input-text"]
}
"""
        ),
        rx.markdown("Клинетский токен, обработчик и аргументы. (Если четсно выглядит не безопасно, но ломать это я не пытался 🤨) После из череди событий оно вытягивается и отправляется на `backend`, где происходит обработка и после отправляется обновлённый `State` по веб-сокету."),
        rx.markdown("`Backend` у `reflex` - это по сути сущности одного типа - `State`. А каждое состояние - это `переменные` (обычные и вычисляемые) и `обаботчики` событий."),
        rx.markdown("Но так же в `backend`'е присутствует надсущность над состяниями - `менеджер` состояний. Благодаря нему всё работает складно и согласовано. Изначально менеджер использует словарь в памяти, но так же можно прикрутить `redis`."),
        rx.markdown(""),
        rx.flex(
            menu_item("Послесловие. После погружения", "arrow-right", "/outro"),
            style={
                "width": "100%",
            },
            justify="end",
        ),
        style={
            "width": "100%",
        },
    )
