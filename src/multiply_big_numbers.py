# coding: utf-8
def multiply(num1: str, num2: str) -> str:
    assert int(num1) >= 0 and int(num2) >= 0
    if len(num1) == 0 or num1 is None or len(num2) == 0 or num2 is None:
        return None

    num1 = [int(i) for i in reversed(num1)]
    num2 = [int(i) for i in reversed(num2)]
    results = []
    for i in num1:
        result = [0 for _ in range(len(num2) + 1)]
        for j in range(len(num2)):
            result[j] += (i * num2[j])
            result[j + 1] += result[j] // 10
            result[j] %= 10
        results.append(result)
    res = [0 for i in range(len(num1) + len(num2) + 1)]
    for i, result in enumerate(results):
        for j in range(len(result)):
            res[i + j] += result[j]
            res[i + j + 1] += res[i + j] // 10
            res[i + j] %= 10
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return "".join(map(str, reversed(res)))


if __name__ == '__main__':
    cases = ((999999999999999999, 99999999999999),
             (0, 999),
             (1, 123),
             (999, 0),
             (0, 0),
             (1, 0),
             (1101, 9),
             (120, 102),
             (1, 1),
             (3, 4))

    for case in cases:
        assert multiply(str(case[0]), str(case[1])) == str(case[0] * case[1])
