from typing import Callable
from lab_3.func_result3 import SearchMethodType, SearchResult
from lab_2.fibonachi import fibonacci
import numpy as np
from lab_3.compute_utils import gradient_calc

def conj_gradient_descend(target: Callable[[np.ndarray], float],
                     x_start: np.ndarray,
                     eps: float = 1e-6,
                     max_iters: int = 1000) -> SearchResult:
    x_prev = x_start.copy()
    x_curr = None
    gradient_last = -1.0 * gradient_calc(target, x_prev, eps)
    iteration = 0
    total_probes = 2 * len(x_prev)
    accuracy = float('inf')
    lm = 1.0
    for iteration in range(max_iters):
        x_curr = x_prev + lm * gradient_last
        result = fibonacci(target, x_prev, x_curr, eps)
        accuracy = min(accuracy, result.accuracy)
        total_probes += result.function_probes

        x_curr = result.result

        gradient_next = gradient_calc(target, x_curr, eps)
        total_probes += 2 * x_prev.size

        w = (np.linalg.norm(gradient_next)**2) / (np.linalg.norm(gradient_last)**2)
        gradient_next = w * gradient_last - gradient_next

        if np.linalg.norm(x_curr - x_prev) < 2 * eps:
            break

        x_prev = x_curr
        gradient_last = gradient_next

    result = SearchResult()
    result.method_type = SearchMethodType.CONJ_GRADIENT_DISCEND
    result.iterations = iteration
    result.function_probes = total_probes
    result.accuracy = accuracy
    result.result = (x_curr + x_prev) / 2

    return result

#