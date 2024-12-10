import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

class UpdateState(rx.State):
    count: int = 0

    @rx.event
    def cool_update(self):
        for i in range(300):
            self.count += 1
            yield


@example # ignore

def yield_upd():
    return rx.vstack(
        rx.text(UpdateState.count, "🦜"),
        rx.button(
            "Count", on_click=UpdateState.cool_update
        ),
    )