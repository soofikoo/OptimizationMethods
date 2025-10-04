from typing import Callable
from lab_1.func_result import SearchResult, SearchMethodType


def golden_ratio(f: Callable[[float], float], lhs: float, rhs: float, eps: float = 1e-6, maxIterations: int = 1000) -> SearchResult:
    iteration = 0
    func_calls = 0
    PSI = 0.61803398874989484820

    if rhs < lhs:
        lhs, rhs = rhs, lhs

    xr = lhs + PSI * (rhs - lhs)
    xl = rhs - PSI * (rhs - lhs)
    fl = f(xl)
    fr = f(xr)
    while iteration < maxIterations:
        if abs(rhs - lhs) < 2*eps:
            break
        iteration += 1
        if fl > fr:
            lhs = xl
            xl = xr
            fl = fr
            xr = lhs + PSI * (rhs - lhs)
            fr = f(xr)
        else:
            rhs = xr
            xr = xl
            fr = fl
            xl = rhs - PSI * (rhs - lhs)
            fl = f(xl)

    result = (lhs + rhs) / 2
    accuracy = abs(rhs - lhs) / 2
    func_calls = iteration + 2
    res = SearchResult(SearchMethodType.GOLDEN_RATIO, iteration, func_calls, accuracy, result)
    return res

if __name__ == "__main__":
    f = lambda x: (x - 1) * (x - 5)
    print(golden_ratio(f, 0, 10))
