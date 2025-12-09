from enum import Enum

class SearchMethodType(Enum):
    BISECTION = "bisection"
    GOLDEN_RATIO = "golden_ratio"
    FIBONACCI = "fibonacci"
    NONE = "none"

class SearchResult:
    method_type: SearchMethodType
    iterations: int
    function_probes: int
    accuracy: float
    result: float

    def __init__(self, method_type: SearchMethodType, iterations: int, function_probes: int, accuracy: float, result: float):
        self.method_type = method_type
        self.iterations = iterations
        self.function_probes = function_probes
        self.accuracy = accuracy
        self.result = result

    def __repr__(self):
        return (f"<Тип метода: {self.method_type.name}, \n"
                f"Количество итераций: {self.iterations}, \n"
                f"Количество вызовов функции: {self.function_probes}, \n"
                f"Точность: {self.accuracy}, \n"
                f"Результат: {self.result}> \n")
