from typing import Callable
from lab_2.func_res import SearchResult, SearchMethodType
import numpy as np

def golden_ratio(target: Callable[[np.ndarray], float], lhs: np.ndarray, rhs: np.ndarray, eps: float = 1e-6, maxIterations: int = 1000) -> SearchResult:
    iteration = 0
    PSI = 0.61803398874989484820

    assert lhs.ndim == 1, 'lhs не одномерный'
    assert rhs.ndim == 1, 'rhs не одномерный'
    assert lhs.size == rhs.size, 'размер lhs и rhs не совпадают'

    xr = lhs + PSI * (rhs - lhs)
    xl = rhs - PSI * (rhs - lhs)
    fl = target(xl)
    fr = target(xr)
    while iteration < maxIterations:
        if np.linalg.norm(rhs - lhs) < 2*eps:
            break
        iteration += 1
        if fl > fr:
            lhs = xl
            xl = xr
            fl = fr
            xr = lhs + PSI * (rhs - lhs)
            fr = target(xr)
        else:
            rhs = xr
            xr = xl
            fr = fl
            xl = rhs - PSI * (rhs - lhs)
            fl = target(xl)

    func_calls = iteration + 2

    res = SearchResult()
    res.method_type = SearchMethodType.GOLDEN_RATIO
    res.iterations = iteration
    res.function_probes = func_calls
    res.accuracy = np.linalg.norm(rhs - lhs) / 2
    res.result = (lhs + rhs) / 2

    return res

if __name__ == "__main__":
    target = lambda x: np.dot(x, (x-1))
    print(golden_ratio(target, np.array([-5, -5, -5]), np.array([5, 5, 5])))