from typing import Callable

import reflex as rx

from ..components.navbar import navbar


def template(
    page: Callable[[], rx.Component]
) -> rx.Component:
    return rx.hstack(
        navbar(),
        rx.vstack(
            rx.container(
                page(),
                style={
                    "width": "100%",
                    "margin-left": "220px",
                }
            ),
            style={
                "width": "100%",
            }
        ),
        style={
            "width": "100%",
            "padding": "100px 250px",
            "gap": "50px",
        }
    )
