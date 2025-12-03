from tools import get_input_list

test = False
text = get_input_list(test)


def get_max_joltage_line(line: str):

    if len(line) == 0:
        return 0
    if len(line) == 1:
        return line[0]

    first = line[0]
    second = line[1]
    for k in range(len(line)):
        if k < len(line) - 1 and int(line[k]) > int(first):
            first = line[k]
            second = line[k + 1]
        elif k > 0 and int(line[k]) > int(second):
            second = line[k]
    return first + second


def get_all_joltage(text: list[str]):
    res = []
    for line in text:
        res.append(get_max_joltage_line(line))
    return res


def main():
    all_jol = get_all_joltage(text)
    res = 0
    for jol in all_jol:
        res += int(jol)
    print(res)


main()
