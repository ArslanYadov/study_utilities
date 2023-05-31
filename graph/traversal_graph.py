from collections import deque
from typing import Callable


def bfs(graph: dict, start_vertex: int, visited: set) -> None:
    """
    Обход графа в ширину.
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
    visited.add(start_vertex)
    queue: deque = deque([start_vertex])
    while queue:
        current_vertex: int = queue.popleft()
        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


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


def count_components(graph: dict, visited: set, traversal: Callable) -> int:
    """
    Подсчет компонент связности для графа.
    На выбор доступно два режима обхода:
        - Depth-First Search (DFS) - обход в глубину;
        - Breadth-First Search (BFS) - обход в ширину.
    ---
    Аргументы:
        - граф в виде списка смежности,
        множество посещенных вершин и метод обхода для графа.
    ---
    Возвращаемое значение:
        - количество компонент связности графа.
    """
    count: int = 0
    for vertex in graph:
        if vertex not in visited:
            traversal(graph, vertex, visited)
            count += 1
    return count


if __name__ == '__main__':

    graph_0: dict = {
        0: {2},
        1: {4},
        2: {0, 3},
        3: {2, 5},
        4: {1},
        5: {2, 3},
        6: set(),
    }

    graph_1: dict = {
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

    test_cases: tuple = (
        (dfs, graph_0, 3),
        (bfs, graph_0, 3),
        (dfs, graph_1, 1),
        (bfs, graph_1, 1),
    )

    for traversal_method, graph, expected_components_number in test_cases:
        visited: set = set()
        assert count_components(graph, visited, traversal_method) == expected_components_number
