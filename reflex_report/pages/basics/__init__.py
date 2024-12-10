from reflex_report.components.code_block import code_block
from reflex_report.components.menu_item import menu_item
from reflex_report.pages.basics.examples import computed_vars, css_props, foreach, long_action, props, setter, state_method, state_method_with_args, state_vars, style_prop, vars_operations, vars_operations_2, yield_upd
from .examples import button, box, html
from ...template.base import template
import reflex as rx


@rx.page(route="/basics", title="👶" * 5)
@template
def index():
    return rx.vstack(
        rx.markdown("# Необходимая база\n"
        "В этом блоке разберём Базу. Ту базу, которую нужно знать для решения 95% задач.\n"
        "# Компоненты\n"),
        rx.markdown("Посмотрим на простенький компонент. Кнопка:"),
        button,
        code_block("reflex_report/pages/basics/examples/button.py"),
        rx.markdown("Эта кнопка просто сущетсвует и ничего не делает. Давайте сделаем более сложный интерфейс и посмотрим, что такое вложенность."),
        rx.markdown("В `reflex` компоненты можно вкладывать друг в друга, так же как в `html`, `React` и т.д."),
        rx.markdown("В `reflex` есть много компонентов-контейнеров. Самый простой `rx.box`"),
        box,
        code_block("reflex_report/pages/basics/examples/box.py"),
        rx.markdown("Если вы знакомы с `html`, то `box` это просто `div`. Он буквально по умолчанию рендериться как `div`. Но если вам такое не подходит, можно использовать любые `html` тэги с помощью `rx.el.*`:"),
        html,
        code_block("reflex_report/pages/basics/examples/html.py"),
        rx.markdown("Но даже если вы не знаете `html`, то `reflex` предлагает большую библиотеку компонентов."),
        rx.markdown("# Стили и Пропсы"),
        rx.markdown("Можно менять содержимое, стили и поведение компонентов с помощью так называемых `props`. Вы могли заметить `kwargs` в примере с `html` - это как раз и есть `props`."),
        rx.markdown("`Props` принимаются как `keyword arguments` при создании компонента. Пример:"),
        props,
        code_block("reflex_report/pages/basics/examples/props.py"),
        rx.markdown("В этом примере мы создаём контейнер `flex` (`flexbox layouts` в `html`) с большими пробелами `gap` и дочерними иконками (`reflex` поддерживает эти иконки `https://lucide.dev/icons`) и фотографией попугая с определённой шириной."),
        rx.markdown("В целом компоненты `reflex` поддерживают большинство стандартных `html` свойств. Например `id: str`, `class_name: list[str]`"),
        code_block("", 
"""
rx.box(
    "Hello World",
    id="box-id",
    class_name=[
        "class-name-1",
        "class-name-2",
    ],
)
"""
        ),
        rx.markdown("`class_name` - список `css` классов, а `id` - обычный `html id`."),
        rx.markdown("Так же `reflex` компоненты часто поддерживают `css props`. Единственное их нужно писать попитонячи в `snake_case`:"),
        css_props,
        code_block("reflex_report/pages/basics/examples/css_props.py"),
        rx.markdown("Тоже самое можно сделать с помощью специального `props`'а `style` эффект будет тот же:"),
        style_prop,
        code_block("reflex_report/pages/basics/examples/style_prop.py"),
        rx.markdown("Так же можно передать в `style` сразу список словарей. Они будут добавлены поочереди."),
        rx.markdown("Окей. Что делать, если не устраивают все стили в `reflex`, ну или другими словами хочется чего-то глобального?"),
        rx.markdown("В `reflex` можно добавить глобальные стили. Для этого можно передать проп `style` при создании приложения:"),
        code_block("",
"""
style = {
    "font_family": "Comic Sans MS",
    "font_size": "20px",
}

app = rx.App(style=style)
"""           
        ),
        rx.markdown("Здесь, мы установили глобальный шрифт и его размер. Так же можно стилизовать отдельные компоненты, передавая их как ключи в словаре и `css` классы:"),
        code_block("",
"""
style = {
    ".css-class": {
        "text_decoration": "underline",
    },
    "#css-for-id": {
        "color": "red",
    },
    rx.text: {
        "background-color": "blue",
    },
}

app = rx.App(style=style)
"""           
        ),
        rx.markdown("Ну и конечно же `reflex` поддерживает `css` файлы. Для этого достаточно передать в `app` список ссылок/относительных путей на `css` файлы в `prop` `stylesheets`"),
        rx.markdown("Так же стоит отметить, что `reflex` поддерживает `tailwind` и `chakra` pseudo styles."),
        rx.markdown("# Отображение данных и динамичекое обновление"),
        rx.markdown("Кажется мы добрались до чего-то интересного. В любом приложении хоть с какой-то логикой нужно хранить и видоизменять данные, делать запросы и так далее. `Redlex` делает это всё в `State` классах."),
        rx.markdown("Чтобы объявить `State` класс достаточно отнаследоваться от `rx.State`:"),
        code_block("",
"""
class ParrotState(rx.State):
    age: int = 2
    name: str = "Kesha"
"""           
        ),
        rx.markdown("На любые поля этого класса можно ссылаться:"),
        state_vars,
        code_block("reflex_report/pages/basics/examples/state_vars.py"),
        rx.markdown("А так же можно ссылаться на методы:"),
        state_method,
        code_block("reflex_report/pages/basics/examples/state_method.py"),
        rx.markdown("Круто, прикольно, и вроде даже работает. Но к сожалению тут допущена \"ошибка\". Любой метод-обработчик событий стоит оборачивать в декоратор `@rx.event` это обеспечивает правильную передачу аргументов и проверки их типов. Тут нам повезло, что никаких аргументов нет."),
        rx.markdown("Окей. А как сделать обработчик с передачей аргументов?"),
        state_method_with_args,
        code_block("reflex_report/pages/basics/examples/state_method_with_args.py"),
        rx.markdown("В этом примере мы добавляем обработчик события `on_blur`, после того, как вы что-то вводите в `input` и выходите из него вызывается этот обработчик, в который передаётся один аргумент - контент поля ввода."),
        rx.markdown("На самом деле, если покапаться в коде библиотеки, то оказывается, что `@rx.event` буквально ничего не делает, только если не добавить аргумент `@rx.event(background=True)`. Для чего нужен `background`? Он позволяет делать такие же обработчики событий, но которые могут выполняться без блокирования пользовательского интерфейса, выполняться фоном. Например можно сделать постоянно обновляемый счётчик."),
        rx.markdown("Говоря про нюансы фоновых задач: Любая фоновая задача должна быть `acync` функцией. Чтобы увидеть текущие фоновые задачи, можно посмотреть на поле `app.background_tasks`. Важно отметить, что одна и та же задача может запускаться несколько раз и иметь дубликаты, `reflex` никак не будет блокировать это. Так же фоновые задачи не могут изменять поля вне блока `async with self`, но могут читать."),
        rx.markdown("### Сеттеры"),
        rx.markdown("В `reflex` предусмотрены сеттеры для полей. Достаточно вызвать метод `YourState.set_<var_name>`. Пример:"),
        setter,
        code_block("reflex_report/pages/basics/examples/setter.py"),
        rx.markdown("## Вычисляемые перменные"),
        rx.markdown("Для удобства в `reflex` существуют так называемые `вычесляемые` перменные. Это такие переменные, значения которых зависят от других перменных. Чтобы объявить такую перменную, надо объявить метод с декоратором `@rx.var`:"),
        computed_vars,
        code_block("reflex_report/pages/basics/examples/computed_vars.py"),
        rx.markdown("Так же к таким переменным можно прикрутить кэш с помощью `@rx.var(cache=True)`"),
        rx.markdown("На самом деле `State` переменные поддерживают достаточно много операций в том числе работу со строками. Так что пример выше можно реализовать и так:"),
        vars_operations,
        code_block("reflex_report/pages/basics/examples/vars_operations.py"),
        rx.markdown("В целом вот основные поддерживаемые операции: сравнения `==`, `>=` и т.д., арифметика `+`, `-`, `%`, `/`, `//`, `*`, возведение в степень `pow()`, модуль `abs()`, булевая логика and `&`, or `|`, not `~`, операции с итерируемыми объектами `.contains()`, `.length()`, `.reverse()`, `.join()` (всё через методы), так же работает индексация `MyState.list_var[idx]`, работа со строками `.to_string()`, `.lower()`, `.upper()`."),
        rx.markdown("Пример со списками:"),
        vars_operations_2,
        code_block("reflex_report/pages/basics/examples/vars_operations_2.py"),
        rx.markdown("Сделаем наш загон с попугаями красивее. В `reflex` можно динамически строить компоненты итерируясь по чему-то, используя `rx.foreach`:"),
        foreach,
        code_block("reflex_report/pages/basics/examples/foreach.py"),
        rx.markdown(""),
        rx.markdown("### События"),
        rx.markdown("В `reflex` сушествует много интересных методов изменения поведения обработчиков событий:"),
        rx.markdown("`rx.prevent_default` как отдельный обработчик или `YourState.method.prevent_default` позволяет обойти действие браузера поумолчанию. Например можно отключить переход по ссылке:"),
        rx.card(
            rx.link(
                "This Link Does Nothing",
                href="https://link.com/",
                on_click=rx.prevent_default,
            ),
            size="5",
            style={
                "width": "100%",
                "display": "flex",
                "justify-content": "center",
            },
        ),
        code_block("",
"""
rx.link(
    "This Link Does Nothing",
    href="https://link.com/",
    on_click=rx.prevent_default,
)
"""           
        ),
        rx.markdown("Аналогично `.stop_propagation` останавливает событие от исполнения на родителе. Если у нас есть `on_click` и на кнопке и на контейнере, при этом на кнопке установлен `.stop_propagation`, то при нажатии на кнопку выполнеться только одно."),
        rx.markdown("`.throttle` позволяет ограничить выполнения собятия по времени. Например событие `.throttle(1000)` ставит минимальный промежуток между вызовами события в секунду. Это полезно например при обработке скроллинга."),
        rx.markdown("`.debounce` даёт возможность добавить `delay` к обработчику события."),
        rx.markdown("### Yield"),
        rx.markdown("Так же для более интересной логики можно использовать `yield` в обработчиках. Работает это примерно так:"),
        yield_upd,
        code_block("reflex_report/pages/basics/examples/yield_upd.py"),
        rx.markdown("На самом деле единственное адекватное применение этомe, на мой взгляд, - это показывать загрузку для долгих операций/запрсов:"),
        long_action,
        code_block("reflex_report/pages/basics/examples/long_action.py"),
        rx.markdown("Так же можно `yield`'ить другие обработчики событий внутри других обработчиков. А ещё можно передавать события в `return`'е. Таким образом получается некоторая цепочка событий."),
        rx.markdown("Стоит отметить, что в `reflex` существуют встроенные ивенты: `rx.console_log`, `rx.scroll_to`, `rx.redirect`, `rx.set_clipboard`, `rx.set_value`, `rx.window_alert`, `rx.download`"),
        rx.markdown("## Страницы"),
        rx.markdown("Мы научились создавать компоненты, делать из них композиции, стилизовать их всеми возможными способами, добавили к ним функционал и прикрутили `backend`, научились динамически обновлять данные."),
        rx.markdown("НО что-то нас останавливает от создания полноценных `web` приложений. Страницы! Как же добавлять страницы?"),
        rx.markdown("В `reflex` существует 2 способа добавлять страницы. Первый: использовать `app.add_page`"),
        code_block("",
"""
def parrot():
    returb rx.text("This is a parrot page! 🦜")

def gorilla():
    return rx.text("This is a gorilla page! 🦍")

app = rx.App()

app.add_page(parrot)
app.add_page(gorilla, route="/gorrilla-route")
"""
        ),
        rx.markdown("В этом блоке кода мы создаём 2 страницы. По умолчанию `route` берёт в качестве значения название функции, но так же можно делать его другим. В данном примере страница `parrot` будет доступна по ссылке `localhost:3000/parrot/`, `gorilla` по `localhost:3000/gorilla-route/`."),
        rx.markdown("Так же при создании страницы можно указать следующие аргументы: `title` (название страницы в браузере, например у этой страницы в названии смайлики), `description` (описание страницы), `image` (иконка страницы), `on_load` (принимает обработчик события Загрузка страницы), `meta` (мета данные страницы в виде `list[dict[str, str]]`)"),
        rx.markdown("Второй способ очень похож на первый. Можно использовать декортатор `@rx.page()`. Вот те же страницы в таком формате:"),
        code_block("",
"""
@rx.page()
def parrot():
    returb rx.text("This is a parrot page! 🦜")

@rx.page(route="/gorilla-route")
def gorilla():
    return rx.text("This is a gorilla page! 🦍")

app = rx.App()
"""
        ),
        rx.markdown("Важно! Если вы создаёте страницы в другом файле, то его обязательно нужно импортировать к `app`."),
        rx.markdown("`@rx.page` принимает такие же аргументы, как `app.add_page`"),
        rx.markdown("Так же ни одно серьёзное приложение не обходиться без динамичесмкого роутинга. "),
        rx.markdown("Чтобы сделать таковой, нужно добавить паттерн с названием поля в квадрпатных скобках в `url`. Например `/parrot/[prrot_id]`, тогда получить нащ `id` можно будет через `rx.State.parrot_id`."),
        rx.markdown("Так же можно получать список параметров `/parrot/eat/[...dishes]` и делать параметры опциональными `/parrot/name/[[...name]]` (здесь единственный нюанс: такой блок можно добавлять только в конек `url`, а первый блок нельзя использовать несколько раз в одном `url`)"),
        rx.flex(
            menu_item("Плавать научились. Теперь можно и понырять", "arrow-right", "/advance"),
            style={
                "width": "100%",
            },
            justify="end",
        ),
        style={
            "width": "100%",
        },
    )
    
