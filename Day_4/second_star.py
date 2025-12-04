from tools import get_input_list
from first_star import is_valid_roll

test = False
text = get_input_list(test)


def remove_roll(text, i, j):
    text[i, j] = "."
    return text


def count_valid_and_replace(text):
    count_valid = 0
    new_text = text.copy()
    for i in range(text.shape[0]):
        for j in range(text.shape[1]):
            if text[i, j] == "@":
                if is_valid_roll(text, i, j):
                    count_valid += 1
                    new_text = remove_roll(text, i, j)
    return new_text, count_valid


def main():
    curr_text,  curr_count = count_valid_and_replace(text)
    count_total_valid = curr_count
    while curr_count:
        curr_text,  curr_count = count_valid_and_replace(curr_text)
        count_total_valid += curr_count
    print(count_total_valid)


main()

    
