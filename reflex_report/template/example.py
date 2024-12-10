from typing import Callable

import reflex as rx


def example(
    comp: Callable[[], rx.Component]
) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.container(comp()),
            style={
                "display": "flex",
                "alignItems": "center",
                "width": "100%",
                "justifyContent": "center",
            }
        ),
        size="5",
        style={
            "width": "100%",
            "justifyContent": "center",
        }
    )