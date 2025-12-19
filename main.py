from typing import Any

import lab_1
import lab_2
import lab_3
import numpy as np

from lab_3.penalty import PenaltyFunction


def test_f(x: float) -> float:
    return x * (x-1.0)

def test_f2(x: np.ndarray) -> float:
    return np.dot(x, (x - 1.0))

def test_f3(x: np.ndarray) -> float:
    return (x[0] - 5) * x[0] + (x[1] - 3) * x[1]


def func_lab_1():
    print({lab_1.bisect(test_f, 0, 10.0)})
    print({lab_1.golden_ratio(test_f, 0, 10.0)})
    print({lab_1.fibonacci(test_f, 0, 10.0, 1e-6)})

def func_lab_2():
    print(lab_2.bisect(test_f2, np.array([-5, -5, -5]), np.array([5, 5, 5])))
    print(lab_2.golden_ratio(test_f2, np.array([-5, -5, -5]), np.array([5, 5, 5])))
    print(lab_2.fibonacci(test_f2, np.array([-5, -5, -5]), np.array([5, 5, 5]), 1.5 * 1e-6))
    print(lab_2.per_cord_descend(test_f2, np.array([0, 0, 0]), 1e-6, 100, 1.0))

def func_lab_3():
    print(lab_3.gradient_descend(test_f3, np.array([0.0, 0.0]), 1e-6, 100))
    print(lab_3.conj_gradient_descend(test_f3, np.array([0.0, 0.0]), 1e-6, 100))
    print(lab_3.newton_raphson(test_f3, np.array([0.0, 0.0]), 1e-6, 100))

    constraints = [
        lambda x: 2 - x[0],  # x >= 2
        lambda x: 1 - x[1],  # y >= 1
        lambda x: x[0] + x[1] - 7  # x + y <= 7
    ]

    eq_constraints = [
        lambda x: x[0] + x[1] - 6  # x + y = 6
    ]

    start = np.array([3.0, 2.0])

    target_in_penalty = PenaltyFunction(test_f3, constraints, 1.0)
    target_ex_penalty = PenaltyFunction(test_f3, constraints, 1.0, eq_constraints)

    print(lab_3.internal_penalty(target_in_penalty, start, 1e-6, 100))
    print(lab_3.external_penalty(target_ex_penalty, start, 1e-6, 100))

if __name__ == "__main__":
    #func_lab_1()
    #func_lab_2()
    func_lab_3()