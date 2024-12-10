import reflex as rx # ignore
# ignore
from reflex_report.template.example import example # ignore
# ignore

@example # ignore
def css_props() -> rx.Component:
    return rx.image(
        src="https://www.columbuszoo.org/sites/default/files/styles/uncropped_xl/public/assets/news/African%20Gray%20Parrot%209833%20-%20Amanda%20Carberry%2C%20Columbus%20Zoo%20and%20Aquarium.jpg?itok=xAm3g1x9",
        width="200px",
        height="auto",
        border_radius="30px 100px",
        border="5px solid lime",
    )