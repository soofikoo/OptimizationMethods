import lab_1
import lab_2
import numpy as np

def test_f(x: float) -> float:
    return x * (x-1)

def test_f2(x: np.ndarray) -> float:
    return np.dot(x, (x-1))

def func_lab_1():
    print({lab_1.bisect(test_f, 0, 10.0)})
    print({lab_1.golden_ratio(test_f, 0, 10.0)})
    print({lab_1.fibonacci(test_f, 0, 10.0, 1e-6)})

def func_lab_2():
    print({lab_2.bisect(test_f2, np.array([-5, -5, -5]), np.array([5, 5, 5]))})
    print({lab_2.golden_ratio(test_f2, np.array([-5, -5, -5]), np.array([5, 5, 5]))})
    print({lab_2.fibonachi(test_f2, np.array([-5, -5, -5]), np.array([5, 5, 5]), 1e-6)})
    print({lab_2.per_cord_descend(test_f2, np.array([0, 0, 0]), 1e-6, 100, 1.0)})

if __name__ == "__main__":
    #func_lab_1()
    func_lab_2()