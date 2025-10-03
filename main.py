from BiSect import bisect


def test_f(x: float) -> float:
    return (x-1)*(x - 5)


a = bisect(test_f, 0.0, 10.0, 1.5e-6, 100)
print(a)