import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

class ParrotEnclosureState(rx.State):
    parrots: list[str] = ["Kesha", "Krosh", "Sancho"]
    new_parrot: str = ""

    @rx.event
    def add_parrot(self) -> None:
        self.parrots.append(self.new_parrot)


@example # ignore
def foreach() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Загон попугаев: ",
            rx.foreach(
                ParrotEnclosureState.parrots,
                lambda parrot: rx.badge(parrot + "🦜", variant="soft", color_scheme="pink"),
            ),
        ),
        rx.text(
            "Всего попугаев в загоне: " + ParrotEnclosureState.parrots.length().to_string(),
        ),
        rx.input(
            default_value=ParrotEnclosureState.new_parrot,
            on_blur=ParrotEnclosureState.set_new_parrot, # тут пока для вас магия
        ),
        rx.button(
            "+",
            on_click=ParrotEnclosureState.add_parrot,
        ),
    )
