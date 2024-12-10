from reflex_report.components.menu_item import menu_item
from ...template.base import template
import reflex as rx


@rx.page(route="/outro", title="🧐" * 5)
@template
def index():
    with open("reflex_report/pages/outro/outro.md", encoding="utf-8") as file:
        content = file.read()

    return rx.vstack(
        rx.markdown(content),
        rx.flex(
            menu_item("Просмотреть сначала 😀", "arrow-right", "/intro"),
            style={
                "width": "100%",
            },
            justify="end",
        ),
    )
