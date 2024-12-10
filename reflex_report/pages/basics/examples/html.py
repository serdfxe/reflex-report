import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

@example # ignore
def html() -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu4UhVTAsWf02a3hjzr0PONrs-cosVFCyToQ&s",
            alt="Попугай"
        ),
        rx.el.p(
            "Хоть попугаи имеют мозг размером с грецкий орех, они очень умные и социальные."
        )
    )