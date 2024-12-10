import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

@example # ignore
def props() -> rx.Component:
    return rx.flex(
        rx.icon(tag="bird"),
        rx.icon(tag="banana"),
        rx.image(
            src="https://ars.els-cdn.com/content/image/3-s2.0-B9780323851251000934-f00093-04-9780323851251.jpg",
            alt="Попугай",
            width="50px",
        ),
        gap="100px",
    )
