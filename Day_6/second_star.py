from tools import get_input_list_second_star
from first_start import apply_operation


test = False
nums, orerations = get_input_list_second_star(test)


def main_second_star():
    res = 0
    for i, operation in enumerate(orerations):
        res += apply_operation(nums[i], operation)
    print(res)


main_second_star()
