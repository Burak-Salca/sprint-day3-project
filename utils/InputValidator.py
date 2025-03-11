def is_valid_number(value: str) -> bool:
    return value.replace(".", "").isdigit()

def is_valid_integer(value: str) -> bool:
    return value.isdigit()

def validate_menu_choice(choice: str, valid_choices: list) -> bool:
    return choice in valid_choices
