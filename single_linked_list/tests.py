import unittest
from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):
    """Класс тестирующий односвязный список."""

    def setUp(self) -> None:
        super().setUp()
        self.linked_list: LinkedList = LinkedList()

    def test_empty_linked_list(self) -> None:
        """Тест пустого односвязного списка."""
        self.assertTrue(self.linked_list.is_empty())
        self.assertEqual(len(self.linked_list), 0)

    def test_convert_iterable_in_linked_list(self) -> None:
        """Проверка конвертации итерируемого объекта в односвязный список."""
        values: list = list(range(1, 6))
        self.linked_list.convert(values)
        self.assertEqual(len(self.linked_list), len(values))
        self.assertFalse(self.linked_list.is_empty())

        words: list = 'spam ham eggs'.split()
        self.linked_list.convert(words)
        self.assertEqual(len(self.linked_list), len(values) + len(words))

    def test_push_back(self) -> None:
        """Тест вставки элемента в конец односвязного списка."""
        item: str = 'spam'
        self.linked_list.push_back(item)
        self.assertEqual(len(self.linked_list), 1)

    def test_push_front(self) -> None:
        """Тест вставки элемента в начало односвязного списка."""
        item: str = 'spam'
        self.linked_list.push_front(item)
        self.assertEqual(len(self.linked_list), 1)


if __name__ == '__main__':

    unittest.main()
