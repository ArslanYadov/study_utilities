def is_acycled(graph: dict) -> bool:
    """
    Проверка графа на ацикличность.
    ---
    Аргументы:
        - граф.
    ---
    Возвращаемое значение:
        - булевское значение ялвляется ли граф ацикличным.
    ---
    Асимптотика: O(V + E), где V - множество вершин,
    а E - множество ребер.
    """
    visited: set = set()

    def dfs(graph: dict, vertex: int, visited: set) -> bool:
        """Depth-First Search."""
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour in visited:
                return False
            return dfs(graph, neighbour, visited)
        return True

    for vertex in graph:
        if vertex not in visited:
            if not dfs(graph, vertex, visited):
                return False
    return True


if __name__ == '__main__':
    import unittest

    class TestTopologicalSort(unittest.TestCase):

        def setUp(self) -> None:
            super().setUp()

            self.graph_0: dict = {
                0: {1, 3, 4},
                1: {4},
                2: {0, 3},
                3: {4},
                4: set()
            }

            self.graph_1: dict = {
                0: {1},
                1: {2},
                2: {3},
                3: set(),
            }

        def test_is_cyclic_graph(self) -> None:
            cases: tuple = (
                self.graph_0,
            )

            for args in cases:
                with self.subTest(args):
                    self.assertFalse(is_acycled(self.graph_0))

        def test_is_acyclic_graph(self) -> None:
            cases: tuple = (
                self.graph_1,
            )

            for args in cases:
                with self.subTest(args):
                    self.assertTrue(is_acycled(self.graph_1))

    unittest.main()
