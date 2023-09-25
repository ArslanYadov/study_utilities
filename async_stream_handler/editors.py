import sys
from collections import deque

from cursor_controls import Cursor


def remove_char() -> None:
    """Удаляет один символ из ввода."""
    Cursor.move_backspase_char()
    sys.stdout.write(' ')
    Cursor.move_backspase_char()


async def redraw_output(items: deque) -> None:
    """Корутина перерисовывает вывод в консоль."""
    Cursor.save_position()
    Cursor.move_on_top()

    for item in items:
        Cursor.delete_line()
        print(item)

    Cursor.restore_position()
