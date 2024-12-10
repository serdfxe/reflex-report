import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

class ParrotState(rx.State):
    name: str = "Kesha"
    surname: str = "Chirikalkin"

    @rx.var
    def fullname(self) -> str:
        return f"{self.name} {self.surname} 🦜"


@example # ignore
def computed_vars() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Полное имя: ",
            ParrotState.fullname,
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