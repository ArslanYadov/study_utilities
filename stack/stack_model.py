from typing import Any


class Stack:
    """Модель стека, основанная на объекте list."""

    def __init__(self) -> None:
        self.__data = []
        self.__top = 0

    def push(self, item) -> None:
        self.__data.append(item)
        self.__top += 1

    def pop(self) -> Any:
        self.__top -= 1
        return self.__data.pop()

    def is_empty(self) -> bool:
        return len(self.__data) == 0

    def top(self) -> int:
        return self.__top


if __name__ == '__main__':

    def test_cases(stack: Stack) -> None:
        nums: list = [1, 2, 3]
        for num in nums:
            stack.push(num)
        assert stack.top() == 3

        while not stack.is_empty():
            item = stack.pop()
            assert item in nums

        assert stack.is_empty()

    stack: Stack = Stack()    
    test_cases(stack)
