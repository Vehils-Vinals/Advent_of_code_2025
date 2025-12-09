from tools import get_input_list


test = False
text = get_input_list(test)


def get_starting_positions(line):
    for i, elt in enumerate(line):
        if elt == "S":
            return i


def transmission(text, i, pos_bars, count):
    res = pos_bars.copy()
    for elt in pos_bars:
        if text[i+1, elt] == "^":
            res.add(elt + 1)
            res.add(elt - 1)
            res.remove(elt)
            count += 1
    return res, count


def main():
    idx_start = get_starting_positions(text[0])
    pos_bar = {idx_start}
    total_count = 0
    for i in range(0, len(text)-1):
        pos_bar, count = transmission(text, i, pos_bar, total_count)
        print(i, count, pos_bar)
        total_count = count
    print(total_count)


# main()
