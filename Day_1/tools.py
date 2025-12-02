def open_file(test=False):

    if test:
        file_name = "test"
    else:
        file_name = "input"

    with open(f"Day_1/{file_name}.txt", "r", encoding="utf-8") as f:
        text = f.read()
    return text


def get_input_list(test):
    res = open_file(test)
    res = res.split("\n")
    return res[:-1]
