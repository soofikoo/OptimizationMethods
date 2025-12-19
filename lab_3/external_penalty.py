from typing import Callable
from lab_3.func_result3 import SearchMethodType, SearchResult
from lab_3.gradient_descend import gradient_descend
import numpy as np

#def external_penalty_func(target, constraints, eq_constraints, x, lam):
#    penalty = 0.0
#
#    for constraint in constraints:
#        fi = constraint(x)
#        fi = max(0.0, fi)
#        penalty += lam * fi**2
#
#    for constraint in eq_constraints:
#        psi = constraint(x)
#        penalty += lam * psi**2
#
#    return target(x) + penalty
#

def external_penalty(target: Callable[[np.ndarray], float],
                     x_start: np.ndarray,
                     eps: float = 1e-6,
                     max_iters: int = 1000) -> SearchResult:
    x_prev = x_start.copy()
    x_curr = None
    lam = 1.0
    iteration = 0
    total_probes = 0

    for iteration in range(max_iters):
        target.lam = lam
        result = gradient_descend(target, x_prev, eps, max_iters)
        x_curr = result.result
        total_probes += result.function_probes

        lam *= 0.5

        if np.linalg.norm(x_curr - x_prev) < 2 * eps:
            break

        x_prev = x_curr

    result = SearchResult()
    result.method_type = SearchMethodType.EXTERNAL_PENALTY
    result.iterations = iteration
    result.function_probes = total_probes
    result.accuracy = np.linalg.norm(x_curr - x_prev) / 2
    result.result = (x_curr + x_prev) / 2

    return result