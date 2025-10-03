from typing import Callable

def bisect(f: Callable[[float], float], lhs: float, rhs: float, eps: float = 1e-6, maxIterations: int = 1000) -> float:
    iteration = 0
    func_calls = 0

    if rhs < lhs:
        temp = 0
        temp = rhs
        rhs = lhs
        lhs = temp

    while iteration < maxIterations:
        if abs(rhs - lhs) < 2 * eps:
            break

        iteration += 1

        xc = (lhs + rhs) / 2
        xl = xc - eps/10
        xr = xc + eps/10

        if f(xl) > f(xr):
            lhs = xl
        else:
            rhs = xr

    result = (lhs + rhs) / 2
    accuracy = abs(rhs - lhs) / 2
    func_calls = iteration * 2

    return result, func_calls, accuracy
if __name__ == "__main__":
    f = lambda x: (x-1)*(x - 5)
    x_min, calls, accur = bisect(f, 0, 10)
    print(f'Минимум найден в точке x = {x_min}')
    print(f'Количество вызовов функции: {calls}')
    print(f'Достигнутая точность: {accur}')
