import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

class ParrotState(rx.State):
    age: int = 2
    name: str = "Kesha"


@example # ignore
def state_vars() -> rx.Component:
    return rx.box(
        rx.image(src="https://lafeber.com/pet-birds/wp-content/uploads/2018/06/Hyacinth-Macaw-300x300.jpg"),
        rx.text(f"Имя попугая: {ParrotState.name}"),
        rx.text(f"Возраст попугая: {ParrotState.age}"),
    )
