import asyncio
import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

class AccoutState(rx.State):
    id: int = 1
    show: bool = True

    @rx.event
    async def increment_id(self):
        self.show = False

        yield

        await asyncio.sleep(1)
        self.show = True

        self.id += 1


@example # ignore
def long_action() -> rx.Component:
    return rx.box(
        rx.button(
            rx.el.img(src=f"https://api.dicebear.com/7.x/miniavs/svg?seed={AccoutState.id}"),
            on_click=AccoutState.increment_id,
            loading=~AccoutState.show,
            style={
                "width": "100px",
                "height": "100px",
            }
        )
    )
