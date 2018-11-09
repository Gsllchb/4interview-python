import copy

N = 8
counter = 0


def arrange_eight_queens():
    chess = [['O' for j in range(N)] for i in range(N)]
    set_queen(chess, N, set(), set(), set())


def set_queen(chess, remain: int, cols: set, diagonal1: set, diagonal2: set) -> None:
    global counter
    if remain == 0:
        print('=' * 20)
        print(counter)
        counter += 1
        for row in chess:
            print(''.join(row))
        return

    y = remain - 1
    for x in range(N):
        if x not in cols and (x - y) not in diagonal1 and (N - 1 - x - y) not in diagonal2:
            new_chess = copy.deepcopy(chess)
            new_chess[y][x] = 'X'
            set_queen(new_chess, remain - 1, cols | {x, }, diagonal1 | {x - y, }, diagonal2 | {N - 1 - x - y, })


if __name__ == '__main__':
    arrange_eight_queens()
