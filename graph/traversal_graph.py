from collections import deque


def bfs(graph: dict, start_vertex: int, destination: int) -> int:
    """
    Обход графа в ширину.
    ---
    Аргументы:
        - граф, начальная вершина и конечная вершина.
    ---
    Возвращаемое значение:
        - количество ребер от начальной вершины до конечной.
    ---
    Асимптотика: O(V + E), где V - множество вершин,
    а E - множество ребер соседних вершин (v1, v2, ..., vn).
    """
    distance: list = [None] * len(graph)
    distance[start_vertex] = 0
    queue: deque = deque([start_vertex])
    while queue:
        current_vertex: int = queue.popleft()
        for neighbour in graph[current_vertex]:
            if distance[neighbour] is None:
                distance[neighbour] = distance[current_vertex] + 1
                queue.append(neighbour)
    return distance[destination]


def dfs(graph: dict, vertex: int, visited: set) -> None:
    """Обход графа в глубину.
    ---
    Аргументы:
        - граф, стартовая вершина и множество посещенных вершин.
    ---
    Возвращаемое значение:
        - None, т.к. происходит только обход графа.
    ---
    Асимптотика: O(V + E), где V - множество вершин,
    а E - множество ребер соседних вершин (v1, v2, ..., vn).
    """
    visited.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


def count_components_dfs(graph: dict, visited: set):
    """
    Подсчет компонент связности для графа,
    используя обход графа в глубину.
    """
    count: int = 0
    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited)
            count += 1
    return count


if __name__ == '__main__':

    graph1: dict = {
        0: {2},
        1: {4},
        2: {0, 3},
        3: {2, 5},
        4: {1},
        5: {2, 3},
        6: set(),
    }
    visited: set = set()
    assert count_components_dfs(graph1, visited) == 3

    graph2: dict = {
        0: {1, 2},              # A
        1: {0, 3, 4},           # B
        2: {0, 4},              # C
        3: {1, 5, 6},           # D
        4: {1, 2, 5, 6, 7},     # E
        5: {3, 4},              # F
        6: {3, 4, 7, 8, 9},     # G
        7: {4, 6, 9, 10},       # H
        8: {6, 9, 11},          # I
        9: {6, 7, 8, 11},       # J
        10: {7},                # K
        11: {8, 9}              # L
    }

    assert bfs(graph2, 0, 11) == 5

    visited: set = set()
    assert count_components_dfs(graph2, visited) == 1
