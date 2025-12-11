def open_file(test=False):

    if test == "test":
        file_name = "test"
    elif test == "test2":
        file_name = "test2"
    else:
        file_name = "input"

    with open(f"Day_11/{file_name}.txt", "r", encoding="utf-8") as f:
        text = f.read()

    return text


def get_dic(line):
    res = {}
    parts = line.split(" ")
    res[parts[0][:-1]] = parts[1:]
    return res


def get_input_list(test):
    res = open_file(test)
    res = res.split("\n")[:-1]

    tmp = [get_dic(elt) for elt in res]

    final_res = {}
    for dic in tmp:
        for key in dic:
            final_res[key] = dic[key]
    return final_res
