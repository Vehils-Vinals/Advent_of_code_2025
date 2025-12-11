from tools import get_input_list


test = False
input_list = get_input_list(test)


def main():
    memo = {}

    def rec(key, seen_mask):
        state = (key, seen_mask)
        if state in memo:
            return memo[state]

        if input_list[key] == ["out"]:
            res = 1 if seen_mask == 0b11 else 0
            memo[state] = res
            return res

        total = 0
        for val in input_list[key]:
            new_mask = seen_mask
            if val == "fft":
                new_mask |= 0b01
            if val == "dac":
                new_mask |= 0b10
            total += rec(val, new_mask)

        memo[state] = total
        return total

    print(rec("svr", 0))


main()
