import shutil
import sys

import global_conf as gc


class Cursor:

    @classmethod
    def move_on_top(cls) -> None:
        """Сдвигает курсор наверх."""
        sys.stdout.write(gc._MOVE_TOP)

    @classmethod
    def move_to_bottom(cls) -> int:
        """Сдвигает курсор вниз."""
        _, rows = shutil.get_terminal_size()
        input_row: str = str(rows - 1)
        move_bottom_code: str = gc._MOVE_BOTTOM.replace('<row>', input_row)
        sys.stdout.write(move_bottom_code)
        return rows

    @classmethod
    def move_backspase_char(cls) -> None:
        """Сдвигает курсор на один символ влево."""
        sys.stdout.write(gc._BACKS_CHAR)

    @classmethod
    def save_position(cls) -> None:
        """Сохраняет позицию курсора."""
        sys.stdout.write(gc._SAVE_POS)

    @classmethod
    def restore_position(cls) -> None:
        """Восстанавливает сохраненную позицию курсора."""
        sys.stdout.write(gc._RESTORE_POS)

    @classmethod
    def delete_line(cls) -> None:
        """Удаляет строку."""
        sys.stdout.write(gc._DEL_LINE)

    @classmethod
    def clear_line(cls) -> None:
        """Очищает строку."""
        sys.stdout.write(gc._CLEAR_LINE)
