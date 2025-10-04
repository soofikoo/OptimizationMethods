from typing import Callable
from lab_1.func_result import SearchMethodType, SearchResult

def fibonacci(f: Callable[[float], float], lhs: float, rhs: float, eps: float = 1e-6) -> SearchResult:
    func_calls = 0

    if rhs < lhs:
        lhs, rhs = rhs, lhs

    fib1 = 1
    fib2 = 1
    iteration = 0
    while fib2 <= (rhs - lhs)/eps:
        temp = fib2
        fib2 = fib1 + fib2
        fib1 = temp
        iteration += 1
    xr = lhs + (fib1 / fib2) * (rhs - lhs)
    xl = lhs + ((fib2 - fib1) / fib2) * (rhs - lhs)
    fl = f(xl)
    fr = f(xr)

    for i in range (iteration):
        fibtemp = fib2
        fib2 = fib1
        fib1 = fibtemp - fib2
        if f(xl) > f(xr):
            lhs = xl
            xl = xr
            fl = fr
            xr = lhs + (fib1 / fib2) * (rhs - lhs)
            if abs(xr - xl) < (rhs - lhs) / 100:
                xr = xr + (rhs - lhs) / 100
            fr = f(xr)
        else:
            rhs = xr
            xr = xl
            fr = fl
            xl = lhs + ((fib2 - fib1) / fib2) * (rhs - lhs)
            if abs(xr - xl) < (rhs - lhs) / 100:
                xl = xl - (rhs - lhs) / 100
            fl = f(xl)

    result = (lhs + rhs) / 2
    accuracy = abs(rhs - lhs) / 2
    func_calls = iteration + 2
    res = SearchResult(SearchMethodType.FIBONACCI, iteration, func_calls, accuracy, result)
    return res

if __name__ == "__main__":
    f = lambda x: (x - 1) * (x - 5)
    print(fibonacci(f, 0, 10))