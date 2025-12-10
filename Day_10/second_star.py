from tools import get_input_list
import pulp
from first_star import get_num


test = False
configs, buttons, voltage = get_input_list(test)


def solve_with_solver(voltage, buttons):
    n = len(voltage)
    m = len(buttons)

    A = [[0] * m for _ in range(n)]
    for j, b in enumerate(buttons):
        for i in get_num(b):
            A[i][j] += 1

    prob = pulp.LpProblem("ButtonsVoltage", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j
         in range(m)]
    prob += pulp.lpSum(x)
    for i in range(n):
        prob += pulp.lpSum(A[i][j] * x[j] for j in range(m)) == voltage[i]
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    if pulp.LpStatus[prob.status] != "Optimal":
        return None
    presses = [int(v.value()) for v in x]
    min_buttons = sum(presses)
    return min_buttons


def main():
    total = 0
    for i in range(len(voltage)):
        min_buttons = solve_with_solver(voltage[i], buttons[i])
        total += min_buttons
    print(total)


main()
