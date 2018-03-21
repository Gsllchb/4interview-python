def find_all_parentheses(n: int, diff: int = 0, parentheses: str = "") -> int:
    if len(parentheses) == 2 * n:
        return [parentheses, ] if diff == 0 else []
    if diff == 0:
        return find_all_parentheses(n, diff + 1, parentheses + '(')
    else:
        return (find_all_parentheses(n, diff + 1, parentheses + '(')
                + find_all_parentheses(n, diff - 1, parentheses + ')'))


if __name__ == '__main__':
    print(find_all_parentheses(3))
    print(find_all_parentheses(0))
    print(find_all_parentheses(1))
