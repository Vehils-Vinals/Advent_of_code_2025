import numpy as np
from tools import get_input_list
from first_star import get_starting_positions


def count_timelines(text: np.ndarray):
    n_rows, n_cols = text.shape
    start_col = get_starting_positions(text[0])
    beams = np.zeros(n_cols, dtype=int)
    beams[start_col] = 1

    for r in range(1, n_rows):
        split_cols = np.where(text[r] == "^")[0]
        if len(split_cols) == 0:
            continue

        new_beams = beams.copy()

        for c in split_cols:
            k = beams[c]
            if k == 0:
                continue
            new_beams[c] -= k
            if c - 1 >= 0:
                new_beams[c - 1] += k
            if c + 1 < n_cols:
                new_beams[c + 1] += k

        beams = new_beams
    return int(beams.sum())


def main(test):
    text = get_input_list(test)
    result = count_timelines(text)
    print(result)


main(False)
