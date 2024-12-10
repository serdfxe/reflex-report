import reflex as rx


def format(lines: list[str]):
    modified_lines = []

    for line in lines:
        if line.strip().endswith('# ignore'):
            continue 

        if line.strip().endswith('# elipsis'):
            modified_lines.append("...\n")
            continue 

        if line.startswith("# "):
            modified_lines.append(line[2:])
            continue
        
        modified_lines.append(line)

    return "".join(modified_lines)

def read_code(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    return lines


def code_block(path: str, code: str = None) -> rx.Component:
    code = read_code(path) if code is None else [i + "\n" for i in code.split("\n")]

    code = format(code)
    
    return rx.card(
        rx.code_block(
            code,
            show_line_numbers=True,
            can_copy=True,
            wrap_long_lines=True,
        ),
        size="5",
        style={
            "width": "100%"
        },
    )
