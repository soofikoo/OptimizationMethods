from enum import Enum
import numpy as np

class SearchMethodType(Enum):
    BISECTION = "bisection"
    GOLDEN_RATIO = "golden_ratio"
    FIBONACCI = "fibonacci"
    PER_CORD_DESCEND ="per_cord"
    NONE = "none"

class SearchResult:
    type: SearchMethodType
    iterations: int
    function_probes: int
    accuracy: float
    result: np.ndarray

    def __init__(self, type: SearchMethodType, iterations: int, function_probes: int, accuracy: float, result: np.ndarray):
        self.type = type
        self.iterations = iterations
        self.function_probes = function_probes
        self.accuracy = accuracy
        self.result = result

    def __repr__(self):
        return (f"<Тип метода: {self.type.name}, \n"
                f"Количество итераций: {self.iterations}, \n"
                f"Количество вызовов функции: {self.function_probes}, \n"
                f"Точность: {self.accuracy}, \n"
                f"Результат: {self.result}> \n")