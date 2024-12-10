import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

links: list[str] = [
    "https://www.lpzoo.org/wp-content/uploads/2023/01/parrot-tall-750x1203.png",
    "https://upload.wikimedia.org/wikipedia/commons/0/05/Parrot.jpg",
    "https://i.ebayimg.com/images/g/s6cAAOSwl2BeTtN9/s-l1200.jpg",
    "https://ars.els-cdn.com/content/image/3-s2.0-B9780323851251000934-f00093-04-9780323851251.jpg",
]

class ParrotState(rx.State):
    link: str = links[-1]


@example # ignore
def setter() -> rx.Component:
    return rx.box(
        rx.image(
            src=ParrotState.link,
            style={
                "height": "200px"
            }
        ),
        rx.select(
            links,
            default_value=ParrotState.link,
            on_change=ParrotState.set_link
        ),
        style={
            "padding": "0 50px",
        },
    )
