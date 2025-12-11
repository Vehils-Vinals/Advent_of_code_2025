from tools import get_input_list


test = False
input_list = get_input_list(test)


def main():
    total = 0

    def rec(key):
        nonlocal total
        if input_list[key] == ["out"]:
            total += 1
            return total
        else:
            for val in input_list[key]:
                total = rec(val)
        return total
    print(rec("you"))


main()
