"""Terminal utils and settings"""

import os
import sys
import termios
import tty


class Terminal:

    def cbrake_mode(self, file_descriptor=sys.stdin) -> None:
        """Переключить терминал на cbrake режим."""
        tty.setcbreak(file_descriptor)

    def save_state(self, file_descriptor=sys.stdin) -> list:
        """Сохраняет состояние терминала."""
        return termios.tcgetattr(file_descriptor)

    def restore_state(self, old_attrs, file_descriptor=sys.stdin) -> None:
        """Восстанавливает состояние терминала."""
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_attrs)

    def clear(self) -> None:
        """Очищает терминал."""
        os.system('clear')
