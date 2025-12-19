from typing import Callable
from lab_3.func_result3 import SearchMethodType, SearchResult
from lab_2.fibonachi import fibonacci
import numpy as np
from lab_3.compute_utils import gradient_calc


def gradient_descend(target: Callable[[np.ndarray], float],
                     x_start: np.ndarray,
                     eps: float = 1e-6,
                     max_iters: int = 1000) -> SearchResult:
    x_prev = x_start.copy()
    x_curr = x_start.copy()
    total_probes = 0
    lm = 1.0

    iteration = 0

    for iteration in range(max_iters):
        gradient = gradient_calc(target, x_prev, eps)
        total_probes += 2 * x_prev.size

        temp = fibonacci(target, x_prev - gradient * lm, x_prev, eps)
        x_curr = temp.result
        total_probes += temp.function_probes
        if np.linalg.norm(x_curr - x_prev) < 2 * eps:
            break
        x_prev = x_curr.copy()

    result = SearchResult()
    result.method_type = SearchMethodType.GRADIENT_DESCEND
    result.iterations = iteration
    result.function_probes = total_probes
    result.accuracy = np.linalg.norm(x_curr - x_prev)/2
    result.result = (x_curr + x_prev)/2

    return result