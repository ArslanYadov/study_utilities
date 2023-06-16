import unittest
from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):
    """Класс тестирующий односвязный список."""

    def setUp(self) -> None:
        super().setUp()
        self.linked_list: LinkedList = LinkedList()

    def test_empty_linked_list(self):
        """Тест пустого односвязного списка."""
        self.assertTrue(self.linked_list.is_empty())
        self.assertEqual(len(self.linked_list), 0)


if __name__ == '__main__':

    unittest.main()
