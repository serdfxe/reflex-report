import reflex as rx

from reflex_report.components.menu_item import menu_item


def navbar() -> rx.Component:
    items = [
        {
            "title": "Введение",
            "href": "/intro",
            "icon": "book-open",
        },
        {
            "title": "Установка",
            "href": "/installation",
            "icon": "arrow-down-to-line",
        },
        {
            "title": "Начало",
            "href": "/start",
            "icon": "rocket",
        },
        {
            "title": "База",
            "href": "/basics",
            "icon": "anvil",
        },
        {
            "title": "Не База",
            "href": "/advance",
            "icon": "chevrons-up",
        },
        {
            "title": "Выведение",
            "href": "/outro",
            "icon": "bird",
        },
    ]

    return rx.card(
        rx.flex(
            *[menu_item(**i) for i in items],
            style={
                "gap": "10px",
                "flex-direction": "column",
                "width": "200px",
            }
        ), 
        size="5",
        style={
            "position": "fixed",  # Фиксированное положение
            "top": "100px",      # Отступ сверху
            "left": "0",         # Фиксировать слева
            "height": "auto",  # Высота с учетом отступа сверху
            "overflow-y": "auto", # Прокрутка по оси Y
            "margin-left": "250px",
        },
    )