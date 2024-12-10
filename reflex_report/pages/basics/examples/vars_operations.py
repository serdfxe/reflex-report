import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

class ParrotState(rx.State):
    name: str = "Kesha"
    surname: str = "Chirikalkin"


@example # ignore
def vars_operations() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Полное имя: ",
            f"{ParrotState.name} {ParrotState.surname} 🦜",
        ),
        rx.input(
            default_value=ParrotState.name,
            on_blur=ParrotState.set_name,
        ),
        rx.input(
            default_value=ParrotState.surname,
            on_blur=ParrotState.set_surname,
        ),
    )