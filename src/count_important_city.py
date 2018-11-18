# coding: utf-8
def main():
    n, m = tuple(int(s) for s in input().split())
    routes = {}
    for _ in range(m):
        u, v = tuple(int(s) for s in input().split())
        if u not in routes:
            routes[u] = []
        routes[u].append(v)

    count = 0
    for city in range(1, n + 1):
        if can_reach(city, routes) < can_be_reached(city, routes, n):
            count += 1
    print(count)


def can_reach(city: int, routes: dict) -> int:
    has_visited = set()
    dfs(routes, city, has_visited, target=-1)
    return len(has_visited)


def dfs(routes: dict, start: int, has_visited: set, target: int) -> bool:
    if start == target:
        return True
    has_visited.add(start)
    if start not in routes:
        return False
    for v in routes[start]:
        if v not in has_visited and dfs(routes, v, has_visited, target):
            return True
    return False


def can_be_reached(city: int, routes: dict, num_city: int) -> int:
    count = 0
    exclude_cities = set()
    for start in range(1, num_city + 1):
        if start in exclude_cities:
            continue
        has_visited = set()
        if dfs(routes, start, has_visited, target=city):
            count += 1
        else:
            exclude_cities.update(has_visited)
    return count


if __name__ == '__main__':
    main()
