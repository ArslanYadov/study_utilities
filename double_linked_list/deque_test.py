import unittest
from deque import Deque


class DequeTest(unittest.TestCase):
    """Test module for Deque model."""

    def setUp(self) -> None:
        super().setUp()
        self.deque: Deque = Deque()

    def test_deque_is_empty(self):
        """Testing for empty deque."""
        self.assertTrue(self.deque.is_empty())
        self.assertEqual(len(self.deque), 0)

    def test_deque_length_after_push_back(self):
        """Check length after push_back method for deque."""
        for i in range(1, 11):
            self.deque.push_back(i)

        self.assertFalse(self.deque.is_empty())
        self.assertEqual(len(self.deque), 10)

    def test_deque_length_after_push_front(self):
        """Check length after push_front method for deque."""
        for i in range(1, 11):
            self.deque.push_front(i)

        self.assertFalse(self.deque.is_empty())
        self.assertEqual(len(self.deque), 10)


if __name__ == '__main__':

    unittest.main()
