import unittest
from deque import Deque


class DequeTest(unittest.TestCase):
    """Test module for Deque model."""

    def setUp(self) -> None:
        super().setUp()
        self.deque: Deque = Deque()

    def test_deque_is_empty(self) -> None:
        """Testing for empty deque."""
        self.assertTrue(self.deque.is_empty())
        self.assertEqual(len(self.deque), 0)

    def test_deque_length_after_push_back(self) -> None:
        """Check length after push_back method for deque."""
        for i in range(1, 11):
            self.deque.push_back(i)

        self.assertFalse(self.deque.is_empty())
        self.assertEqual(len(self.deque), 10)

    def test_deque_length_after_push_front(self) -> None:
        """Check length after push_front method for deque."""
        for i in range(1, 11):
            self.deque.push_front(i)

        self.assertFalse(self.deque.is_empty())
        self.assertEqual(len(self.deque), 10)

    def test_pop_item_from_end(self) -> None:
        """Testing pop item from the end of deque."""
        items: list = list(range(1, 11))

        for item in items:
            self.deque.push_back(item)

        for expected in items[::-1]:
            self.assertEqual(self.deque.pop_back(), expected)
        self.assertTrue(self.deque.is_empty())

    def test_pop_item_from_front(self) -> None:
        """Testing pop item from the front of deque."""
        items: list = list(range(1, 11))

        for item in items:
            self.deque.push_back(item)

        for expected in items:
            self.assertEqual(self.deque.pop_front(), expected)
        self.assertTrue(self.deque.is_empty())


if __name__ == '__main__':

    unittest.main()
