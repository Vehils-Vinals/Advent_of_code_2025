from tools import get_input_list
from itertools import combinations

test = False
configs, buttons, voltage = get_input_list(test)


def get_num(button):
    return [int(x) for x in button.strip("()").split(",")]


def check_one_sequence(config: str, combination_button: list[str]):
    n = len(config)
    new_config = ["." for _ in range(n)]

    for b in combination_button:
        int_b = get_num(b)
        for i in int_b:
            if new_config[i] == ".":
                new_config[i] = "#"
            else:
                new_config[i] = "."
    return "".join(new_config) == config


def get_min_buttons(config: str, buttons: list[str]):
    n_comb = len(buttons)
    for i in range(1, n_comb):
        all_cominaison = combinations(buttons, i)
        for comb in all_cominaison:
            if check_one_sequence(config, comb):
                return i


def main():
    total = 0
    for i in range(len(configs)):
        config = configs[i]
        button = buttons[i]
        min_buttons = get_min_buttons(config, button)
        total += min_buttons
    print(total)


# main()
