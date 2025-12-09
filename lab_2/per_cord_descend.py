from typing import Callable
from lab_2 import fibonacci
from lab_2.func_res import SearchMethodType, SearchResult
import numpy as np

def per_cord_descend(target: Callable[[np.ndarray], float], x0: np.ndarray, eps: float = 1e-6, maxIterations: int = 1000, lm: float = 0.1) -> SearchResult:
    x = np.copy(x0)
    n = len(x)
    probs = 0
    opt_coord = 0
    x_next = 0
    x_prev = 0
    iteration_count = 0
    current_coord = 0
    for iteration in range(maxIterations):
        iteration_count += 1
        current_coord = iteration % n
        e_i = np.zeros(n)
        e_i[current_coord] = 1.0
        x_prev = np.copy(x)

        x_left = x - eps * e_i
        x_right = x + eps * e_i

        f_left = target(x_left)
        f_right = target(x_right)
        probs += 2

        if f_left > f_right:
            search_interval = [x, x + lm * e_i]
        else:
            search_interval = [x - lm * e_i, x]

        res = fibonacci(target, *search_interval, eps)
        x_next = res.result
        probs += res.function_probes

        x = np.copy(x_next)
        if abs(x_next[current_coord] - x_prev[current_coord]) < 2*eps:
            opt_coord += 1
        else:
            opt_coord = 0
        if opt_coord == n:
            break


    result = SearchResult()
    result.method_type = SearchMethodType.PER_CORD_DESCEND
    result.iterations = iteration_count
    result.function_probes = probs
    result.accuracy = abs(x_next[current_coord] - x_prev[current_coord])
    result.result = x_next
    
    return result