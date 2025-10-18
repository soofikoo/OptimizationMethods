from typing import Callable
from lab_1.func_result import SearchMethodType, SearchResult
import numpy as np

def fibonachi(f: Callable[[np.ndarray], float], lhs: np.ndarray, rhs: np.ndarray, eps: float = 1e-6) -> SearchResult:
    assert lhs.ndim == 1, 'lhs не одномерный'
    assert rhs.ndim == 1, 'rhs не одномерный'
    assert lhs.size == rhs.size, 'размер lhs и rhs не совпадают'

    fib1, fib2 = 1.0, 1.0
    iteration = 0
    condition = (np.linalg.norm(rhs - lhs))/eps
    while fib2 <= condition:
        fib2, fib1 = fib1 + fib2, fib2
        iteration += 1
    xr = lhs + (fib1 / fib2) * (rhs - lhs)
    xl = lhs + ((fib2 - fib1) / fib2) * (rhs - lhs)
    fl = f(xl)
    fr = f(xr)

    for _ in range (iteration):
        fib2, fib1 = fib1, fib2 - fib1

        if f(xl) > f(xr):
            lhs = xl
            xl = xr
            fl = fr
            xr = lhs + (fib1 / fib2) * (rhs - lhs)
            fr = f(xr)
        else:
            rhs = xr
            xr = xl
            fr = fl
            xl = lhs + ((fib2 - fib1) / fib2) * (rhs - lhs)
            fl = f(xl)

    result = (lhs + rhs) / 2
    accuracy = np.linalg.norm(rhs - lhs) / 2
    func_calls = iteration + 2
    res = SearchResult(SearchMethodType.FIBONACCI, iteration, func_calls, accuracy, result)
    return res

if __name__ == "__main__":
    f = lambda x: np.dot(x, (x-1))
    print(fibonachi(f, np.array([-5, -5, -5]), np.array([5, 5, 5])))