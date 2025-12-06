import numpy as np


def open_file(test=False):

    if test:
        file_name = "test"
    else:
        file_name = "input"

    with open(f"Day_6/{file_name}.txt", "r", encoding="utf-8") as f:
        text = f.read()

    return text


def get_operation(text):
    res = []
    for ch in text[-1]:
        if ch == " ":
            continue
        elif ch in {"+", "-", "*", "/"}:
            res.append(ch)
    return res


def get_input_list_first_star(test):
    res = open_file(test)
    res = res.split("\n")[:-1]

    operations = get_operation(res)

    nums = np.zeros((len(operations), len(res) - 1), dtype=int)
    for i, elt in enumerate(res[:-1]):
        j = 0
        tmp = elt.split(" ")
        for el in tmp:
            if el != "":
                nums[j, i] = int(el)
                j += 1
    return nums, operations


def get_columns(text):
    res = np.empty((len(text[0]), len(text)), dtype=str)
    for i, line in enumerate(text):
        for j, ch in enumerate(line):
            res[j, i] = ch
    return res


def get_nums(li_col):
    res = []
    problem = []
    for elt in li_col:
        num = ""
        for ch in elt:
            if ch != " ":
                num += ch
        if num != "":
            problem.append(int(num))
        else:
            res.append(problem)
            problem = []
    res.append(problem)
    return res


def get_input_list_second_star(test):
    res = open_file(test)
    res = res.split("\n")[:-1]

    operations = get_operation(res)
    nums = get_nums(get_columns(res[:-1]))
    return nums, operations
