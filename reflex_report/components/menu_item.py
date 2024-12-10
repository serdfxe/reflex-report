import reflex as rx


def menu_item(title: str, icon: rx.Component, href: str) -> rx.Component:
    return rx.link(rx.hstack(
            rx.icon(icon),
            rx.text(title),
            spacing="5",
            cursor="pointer",   
        ),
        href=href)