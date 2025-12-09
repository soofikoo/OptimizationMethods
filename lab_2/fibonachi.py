from typing import Callable
from lab_2.func_res import SearchMethodType, SearchResult
import numpy as np


def fibonacci_next(f_curr: float, f_next: float) -> tuple[float, float]:
    f_next, f_curr = f_next + f_curr, f_next
    return f_curr, f_next

def fibonacci_prev(f_curr: float, f_next: float) -> tuple[float, float]:
    f_next, f_curr = f_curr, f_next - f_curr
    return f_curr, f_next


def fibonacci(target: Callable[[np.ndarray], float], lhs: np.ndarray, rhs: np.ndarray, eps: float = 1e-6) -> SearchResult:
    assert lhs.ndim == 1, 'lhs не одномерный'
    assert rhs.ndim == 1, 'rhs не одномерный'
    assert lhs.size == rhs.size, 'размер lhs и rhs не совпадают'

    fib1, fib2 = 1.0, 1.0
    iteration = 0
    condition = (np.linalg.norm(rhs - lhs))/eps
    while fib2 <= condition:
        fib1, fib2 = fibonacci_next(fib1, fib2)
        iteration += 1
    xr = lhs + (fib1 / fib2) * (rhs - lhs)
    xl = lhs + ((fib2 - fib1) / fib2) * (rhs - lhs)
    fl = target(xl)
    fr = target(xr)

    for _ in range (iteration):
        fib1, fib2 = fibonacci_prev(fib1, fib2)

        if target(xl) > target(xr):
            lhs = xl
            xl = xr
            fl = fr
            xr = lhs + (fib1 / fib2) * (rhs - lhs)
            fr = target(xr)
        else:
            rhs = xr
            xr = xl
            fr = fl
            xl = lhs + ((fib2 - fib1) / fib2) * (rhs - lhs)
            fl = target(xl)

    func_calls = iteration + 2
    res = SearchResult()
    res.method_type = SearchMethodType.FIBONACCI
    res.iterations = iteration
    res.function_probes = func_calls
    res.accuracy = np.linalg.norm(rhs - lhs) / 2
    res.result = (lhs + rhs) / 2
    return res

if __name__ == "__main__":
    target = lambda x: np.dot(x, (x-1))
    print(fibonacci(target, np.array([-5, -5, -5]), np.array([5, 5, 5])))