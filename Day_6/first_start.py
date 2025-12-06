from tools import get_input_list_first_star

test = False
nums, operations = get_input_list_first_star(test)


def apply_operation(line: list[int], operation: str):
    res = line[0]
    for elt in line[1:]:
        if operation == "+":
            res += elt
        elif operation == "-":
            res -= elt
        elif operation == "*":
            res *= elt
        elif operation == "/":
            res /= elt
    return res


def main_first_star():
    res = 0
    for i, operation in enumerate(operations):
        res += apply_operation(nums[i, :], operation)
    print(res)


# main_first_star()
