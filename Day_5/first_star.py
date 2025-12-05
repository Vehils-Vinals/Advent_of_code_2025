from tools import get_input_list


test = False
ranges, foods = get_input_list(test)


def is_in_range(min_i: int, max_i: int, target: int):
    return (min_i <= target <= max_i)


def is_food_good(ranges: list, food: str):
    for elt in ranges:
        min_max = elt.split("-")
        min_i, max_i = int(min_max[0]), int(min_max[1])
        if is_in_range(min_i, max_i, int(food)):
            return True
    return False


def main():
    count_fresh = 0
    for food in foods:
        if is_food_good(range, food):
            count_fresh += 1
    print(count_fresh)


main()
