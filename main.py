import lab_1

def test_f(x: float) -> float:
    return (x - 1) * (x - 5)


def func_lab_1():
    print(f'bisect result      : {lab_1.bisect(test_f, 0, 10.0)}\n')
    print(f'golden_ratio result: {lab_1.golden_ratio(test_f, 0, 10.0)}\n')
    print(f'fibonacci result   : {lab_1.fibonacci(test_f, 0, 10.0, 1e-6)}')

if __name__ == "__main__":
    func_lab_1()