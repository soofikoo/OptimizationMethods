from enum import Enum
import numpy as np

class SearchMethodType(Enum):
    BISECTION = "bisection"
    GOLDEN_RATIO = "golden_ratio"
    FIBONACCI = "fibonacci"
    PER_CORD_DESCEND ="per_cord"
    NONE = "none"


def exception_catcher(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper



class SearchResult:
    def __init__(self):
        self._method_type: SearchMethodType = SearchMethodType.NONE
        self._iterations: int = 0
        self._function_probes: int = 0
        self._accuracy: float = 0.0
        self._result: np.ndarray = np.array([])

    @property
    def method_type(self) -> SearchMethodType:
        return self._method_type

    @property
    def iterations(self) -> int:
        return self._iterations

    @property
    def function_probes(self) -> int:
        return self._function_probes

    @property
    def accuracy(self) -> float:
        return self._accuracy

    @property
    def result(self) -> np.ndarray:
        return self._result

    @method_type.setter
    def method_type(self, method_type: SearchMethodType):
        if isinstance(method_type, SearchMethodType):
            self._method_type = method_type

    @iterations.setter
    def iterations(self, iterations: int):
        self._iterations = int(iterations)

    @function_probes.setter
    def function_probes(self, function_probes: int):
        self._function_probes = int(function_probes)

    @accuracy.setter
    def accuracy(self, accuracy: float):
        self._accuracy = float(accuracy)

    @result.setter
    def result(self, result: np.ndarray):
        self._result = np.array(result)

    def clear(self):
        self._method_type = SearchMethodType.NONE
        self._iterations = 0
        self._function_probes = 0
        self._accuracy = 0
        self._result = np.array([])

    def __str__(self):
        return (f"\n"
                f"\tMethodType:     {self.method_type}, \n"
                f"\tIterations:     {self.iterations}, \n"
                f"\tFunctionProbes: {self.function_probes}, \n"
                f"\tAccuracy:       {self.accuracy}, \n"
                f"\tResult:         [{', '.join(str(v) for v in self.result.flat)}]\n")

    __repr__ = __str__


if __name__ == "__main__":
    res = SearchResult()
    print(repr(res))
    res.method_type = 123
    print(str(res))
