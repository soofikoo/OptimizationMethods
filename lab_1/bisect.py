from typing import Callable
from lab_1.func_result import SearchMethodType, SearchResult


def bisect(f: Callable[[float], float], lhs: float, rhs: float, eps: float = 1e-6, maxIterations: int = 1000) -> SearchResult:
    iteration = 0
    func_calls = 0

    if rhs < lhs:
        lhs, rhs = rhs, lhs

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
    res = SearchResult(SearchMethodType.BISECTION, iteration, func_calls, accuracy, result)
    return res

if __name__ == "__main__":
    f = lambda x: (x-1)*(x - 5)
    print(bisect(f, 0, 10))