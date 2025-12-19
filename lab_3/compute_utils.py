from typing import Callable
import numpy as np

def partial(function: Callable[[np.ndarray], float], x: np.ndarray, index: int = 0, dx: float = 1e-6) -> float:
    x[index] -= dx
    fl = function(x)
    x[index] += 2 * dx
    fr = function(x)
    x[index] -= dx
    return (fr - fl) / (2 * dx)

def gradient_calc(function: Callable[[np.ndarray], float], x: np.ndarray, eps) -> np.ndarray:
    return np.array(tuple(partial(function, x, index, eps) for index in range(x.size)))

def hessian(target, x, h=1e-5):
    n = len(x)
    H = np.zeros((n, n))
    fx = target(x)

    for i in range(n):
        for j in range(n):
            x_ijp = x.copy()
            x_ijp[i] += h
            x_ijp[j] += h

            x_ip = x.copy()
            x_ip[i] += h

            x_jp = x.copy()
            x_jp[j] += h

            H[i, j] = (target(x_ijp) - target(x_ip) - target(x_jp) + fx) / (h**2)
    return H