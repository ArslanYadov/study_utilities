def topological_sort(graph: dict) -> list:
    """
    Топологическая сортировка ориентированного, ацикличного графа.
    ---
    Аргументы:
        - граф.
    ---
    Возвращаемое значение:
        - список вершин, отсортированный в топологическом порядке.
    ---
    Асимптотика: O(V + E), где V - множество вершин,
    а E - множество ребер.
    """
    def dfs(graph: dict, vertex: int) -> None:
        """Depth-First Search."""
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                dfs(graph, neighbour)
        in_order.append(vertex)

    visited: set = set()
    in_order: list = []
    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex)
    return in_order[::-1]


if __name__ == '__main__':
    import unittest

    class TestTopologicalSort(unittest.TestCase):

        def setUp(self) -> None:
            super().setUp()

            self.graph_0: dict = {
                1: {2, 4},
                2: {3, 4},
                3: {5},
                4: {3},
                5: set(),
            }

            self.graph_1: dict = {
                0: set(),
                1: set(),
                2: {3},
                3: {1},
                4: {0, 1},
                5: {2, 0},
            }

        def test_topological_sorting(self) -> None:
            cases: tuple = (
                (self.graph_0, [1, 2, 4, 3, 5]),
                (self.graph_1, [5, 4, 2, 3, 1, 0])
            )

            for args, expected in cases:
                with self.subTest(args):
                    self.assertEqual(topological_sort(args), expected)

    unittest.main()
