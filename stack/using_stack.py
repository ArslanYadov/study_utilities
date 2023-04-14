"""
File: using_stack.py
---
Description: Некоторые алгоритмы, которые подходят для использования стека.
---
1. Алгоритм проверки правильной скобочной последовательности.
2. Алгоритм вычисления выражения в постфиксной нотации (ОПН).
"""
from stack_model import Stack
from typing import Callable


def is_braces_sequence_correct(braces_sequence: str) -> bool:
    """Проверка правильной скобочной последовательности."""
    stack: Stack = Stack()
    for brace in braces_sequence:
        if brace in '({[':
            stack.push(brace)
        else:
            if stack.is_empty():
                return False
            last = stack.pop()
            if (
                brace == ')' and last != '('
                or brace == '}' and last != '{'
                or brace == ']' and last != '['
            ):
                return False

    return stack.is_empty()


def calc(x: int, y: int, sign: str) -> int:
    """Вычисление выражения в зависимости от знака."""
    expression: dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    return expression[sign](x, y)


def reverse_polish_notation(expression: list) -> int:
    """Обратная польская нотация."""
    stack: Stack = Stack()
    for token in expression:
        if isinstance(token, int):
            stack.push(token)
        else:
            y: int = stack.pop()
            x: int = stack.pop()
            stack.push(calc(x, y, token))
    return stack.pop()


if __name__ == '__main__':

    def test_cases(cases: dict, func: Callable) -> None:
        for args, expected in cases.items():
            assert func(args) == expected, args

    braces: dict = {
        '(([()]))[]': True,
        '([)]': False,
        '([]': False,
        '}': False,
        '[{()}]': True,
    }

    test_cases(braces, is_braces_sequence_correct)

    rpolska_notation: dict = {
        (5, 2, '+'): 7,
        (2, 7, '+', 5, '*'): 45,
        (2, 7, 5, '*', '+'): 37,
    }

    test_cases(rpolska_notation, reverse_polish_notation)
