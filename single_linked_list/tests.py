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

    def test_pop_back(self) -> None:
        """Тест удаления элемента из конца односвязного списка."""
        values: list = list(range(1, 11))
        self.linked_list.convert(values)

        for val in reversed(values):
            if self.linked_list.is_empty():
                break

            self.assertEqual(self.linked_list.pop_back(), val)
        self.assertTrue(self.linked_list.is_empty())

    def test_pop_front(self) -> None:
        """Тест удаления элемента из начала односвязного списка."""
        words: list = 'spam ham eggs'.split()
        self.linked_list.convert(words)

        life_meaning: str = '42'
        words.append(life_meaning)
        self.linked_list.push_back(life_meaning)

        for word in words:
            if self.linked_list.is_empty():
                break

            self.assertEqual(self.linked_list.pop_front(), word)
        self.assertTrue(self.linked_list.is_empty())

    def test_item_in_linked_list(self) -> None:
        """Тест работы дандер метода __contains__: key in object."""
        string: str = 'Nobody expects the Spanish Inquisition'
        words: list = string.lower().split()
        self.linked_list.convert(words)
        for word in words:
            self.assertIn(word, self.linked_list)
        self.assertNotIn(42, self.linked_list)


if __name__ == '__main__':

    unittest.main()
