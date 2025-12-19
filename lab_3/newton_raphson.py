from typing import Callable
from lab_3.func_result3 import SearchMethodType, SearchResult
import numpy as np
from lab_3.compute_utils import gradient_calc, hessian

def newton_raphson(target: Callable[[np.ndarray], float],
                     x_start: np.ndarray,
                     eps: float = 1e-6,
                     max_iters: int = 1000) -> SearchResult:
    x_curr = x_start.copy()
    x_prev = x_start.copy()
    iteration = 0
    total_probes = 0

    for iteration in range(max_iters):
        grad = gradient_calc(target, x_prev, eps)
        hess_inv = np.linalg.inv(hessian(target, x_prev))

        x_curr = x_prev - hess_inv @ grad
        total_probes += 2 * x_prev.size + x_prev.size ** 2

        if np.linalg.norm(x_curr - x_prev) < 2 * eps:
            break

        x_prev = x_curr

    result = SearchResult()
    result.method_type = SearchMethodType.NEWTON_RAPHSON
    result.iterations = iteration
    result.function_probes = total_probes
    result.accuracy = np.linalg.norm(x_curr - x_prev) / 2
    result.result = (x_curr + x_prev) / 2

    return result