from typing import Callable
from lab_2.func_res import SearchMethodType, SearchResult
import numpy as np

def bisect(target: Callable[[np.ndarray], float], lhs: np.ndarray, rhs: np.ndarray, eps: float = 1e-6, maxIterations: int = 1000) -> SearchResult:
    iteration = 0
    assert lhs.ndim == 1, 'lhs не одномерный'
    assert rhs.ndim == 1, 'rhs не одномерный'
    assert lhs.size == rhs.size, 'размер lhs и rhs не совпадают'

    dir = ((rhs - lhs) * eps)/(10 * np.linalg.norm(rhs - lhs))

    while iteration < maxIterations:
        if np.linalg.norm(rhs - lhs) < 2 * eps:
            break

        iteration += 1

        xc = (lhs + rhs) / 2
        xl = xc - dir
        xr = xc + dir

        if target(xl) > target(xr):
            lhs = xl
        else:
            rhs = xr

    func_calls = iteration * 2
    res = SearchResult()
    res.method_type = SearchMethodType.BISECTION
    res.iterations = iteration
    res.function_probes = func_calls
    res.accuracy = np.linalg.norm(rhs - lhs) / 2
    res.result = (lhs + rhs) / 2
    return res

if __name__ == "__main__":
    target = lambda x: np.dot(x, (x-1))
    print(bisect(target, np.array([-5.0, -5.0, -5.0]), np.array([5.0, 5.0, 5.0])))