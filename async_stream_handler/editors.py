import sys
from collections import deque

import cursor_controls as cursor


def remove_char() -> None:
    """Удаляет один символ из ввода."""
    cursor.move_backspase_char()
    sys.stdout.write(' ')
    cursor.move_backspase_char()


async def redraw_output(items: deque) -> None:
    """Корутина перерисовывает вывод в консоль."""
    cursor.save_cursor_position()
    cursor.move_cursor_on_top()

    for item in items:
        cursor.delete_line()
        print(item)

    cursor.restore_cursor_position()
