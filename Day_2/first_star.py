from tools import get_input_list
import numpy as np

test = True
text = get_input_list(test)


def is_valid_first_star(s: str):
    n = len(s)
    if n == 0:
        return False
    if n % 2 == 1:
        return True
    if s[:n//2] == s[n//2:]:
        return False
    return True


def get_false_id_range(min_range, max_range):
    res = []
    for k in range(min_range, max_range + 1):
        if not is_valid_first_star(str(k)):
            res.append(int(k))
    return res


def main():
    res = []
    for s in text:
        min_range, max_range = s.split("-")[0], s.split("-")[1]
        res.extend(get_false_id_range(int(min_range), int(max_range)))
    print(np.sum(res))


main()
