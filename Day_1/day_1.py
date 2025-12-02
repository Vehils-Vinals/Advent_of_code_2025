from tools import get_input_list

test = False
text = get_input_list(test)

dic_dir = {"L": -1, "R": 1}


def first_star():
    pos = 50
    count_code = 0
    for s in text:
        dir = dic_dir[s[0]]
        dist = int(s[1:])
        pos = (pos + dir * dist) % 100

        if pos == 0:
            count_code += 1
    return count_code


def second_star():
    pos = 50
    count_code = 0
    for s in text:

        dir = dic_dir[s[0]]
        dist = int(s[1:])

        delta = dir * dist
        total = abs(delta)

        if delta > 0:
            steps_to_zero = (100 - pos) % 100
        else:
            steps_to_zero = pos % 100

        if steps_to_zero == 0:
            steps_to_zero = 100

        remaining = total - steps_to_zero
        if remaining >= 0:
            count_code += 1 + remaining // 100

        pos = (pos + delta) % 100

    return count_code


print(second_star())
