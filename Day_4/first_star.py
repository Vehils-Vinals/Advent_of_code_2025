from tools import get_input_list

test = False
text = get_input_list(test)


directions = {(1, 1), (1, -1), (-1, 1), (-1, -1),
              (0, 1), (0, -1), (1, 0), (-1, 0)}


def is_valid_roll(text: str, i: int, j: int):
    count_roll = 0
    for dir in directions:
        if (dir[0] + i >= 0 and dir[0] + i < text.shape[0] and
           dir[1] + j >= 0 and dir[1] + j < text.shape[1]):
            if text[i + dir[0], j + dir[1]] == '@':
                count_roll += 1
    return (count_roll < 4) * 1


def main():
    count_valid = 0
    for i in range(text.shape[0]):
        for j in range(text.shape[1]):
            if text[i, j] == "@":
                count_valid += is_valid_roll(text, i, j)
    print(count_valid)


# main()
