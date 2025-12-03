from tools import get_input_list

test = False
text = get_input_list(test)


def shift(l1: list, l2: list, k: int):
    res = l1
    for i in range(len(l1)):
        res[i] = l2[k + i + 1]
    return res


def update_pos(pos: list, k: int):
    res = pos
    for i in range(len(pos)):
        res[i] = k + i
    return res


def get_all_12_joltage_line(line: str, n: int = 12):
    power_units = []
    for i in range(n):
        power_units.append(line[i])
    pos = [i for i in range(12)]

    for k in range(len(line)):
        for i in range(len(power_units)):
            if (i - 1 < k < len(line) - (n - i - 1) and
               int(power_units[i]) < int(line[k]) and
               pos[i] < k):

                power_units[i] = line[k]
                power_units[i+1:] = shift(power_units[i+1:], line, k)
                pos[i:] = update_pos(pos[i:], k)
                break
    return "".join(power_units)


def get_all_joltage(text: list[str]):
    res = []
    for line in text:
        res.append(get_all_12_joltage_line(line))
    return res


def main():
    all_jol = get_all_joltage(text)
    res = 0
    for jol in all_jol:
        res += int(jol)
    print(res)


main()
