def get_range(text: str):
    range = []
    i = 0
    while i < len(text):
        if text[i] == "":
            i += 1
            return range, i
        range.append(text[i])
        i += 1
    return range, i


def get_food(text: str, i: int):
    return text[i:]


def open_file(test=False):

    if test:
        file_name = "test"
    else:
        file_name = "input"

    with open(f"Day_5/{file_name}.txt", "r", encoding="utf-8") as f:
        text = f.read()

    return text


def get_input_list(test):
    res = open_file(test)
    res = res.split("\n")[:-1]

    range, i = get_range(res)
    food = get_food(res, i)

    return range, food
