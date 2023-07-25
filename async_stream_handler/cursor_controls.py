import shutil
import sys

import global_conf as gc


def save_cursor_position() -> None:
    """Сохраняет позицию курсора."""
    sys.stdout.write(gc._SAVE_POS)


def restore_cursor_position() -> None:
    """Восстанавливает сохраненную позицию курсора."""
    sys.stdout.write(gc._RESTORE_POS)


def move_cursor_on_top() -> None:
    """Сдвигает курсор наверх."""
    sys.stdout.write(gc._MOVE_TOP)


def delete_line() -> None:
    """Удаляет строку."""
    sys.stdout.write(gc._DEL_LINE)


def clear_line() -> None:
    """Очищает строку."""
    sys.stdout.write(gc._CLEAR_LINE)


def move_backspase_char() -> None:
    """Сдвигает каретку на один символ."""
    sys.stdout.write(gc._BACKS_CHAR)


def move_cursor_to_bottom() -> int:
    """Сдвигает каретку вниз."""
    _, rows = shutil.get_terminal_size()
    input_row: str = str(rows - 1)
    move_bottom_code: str = gc._MOVE_BOTTOM.replace('<row>', input_row)
    sys.stdout.write(move_bottom_code)
    return rows
