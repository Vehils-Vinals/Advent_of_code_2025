def open_file(test=False):

    if test:
        file_name = "test"
    else:
        file_name = "input"

    with open(f"Day_10/{file_name}.txt", "r", encoding="utf-8") as f:
        text = f.read()

    return text


def get_voltage_list(voltage):
    return [int(x) for x in voltage.strip("{}").split(",")]


def get_input_list(test):
    res = open_file(test)
    res = res.split("\n")[:-1]

    configs = [line.split(" ")[0][1: -1] for line in res]
    buttons = [line.split(" ")[1:-1] for line in res]
    voltages = [line.split(" ")[-1] for line in res]

    return configs, buttons, [get_voltage_list(voltage) for voltage
                              in voltages]
