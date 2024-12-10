import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

@example # ignore
def box() -> rx.Component:
    return rx.box(
        rx.text("Hello world!"),
        rx.button("😀")
    )
