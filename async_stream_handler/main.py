import asyncio

import cursor_controls as cursor
import termus as terminal
from editors import redraw_output
from readers import create_stdin_reader, read_line
from storages import MessageStore
from time_utils import sleeper


async def main() -> None:
    old_terminal: list = terminal.save_terminal_state()

    try:
        terminal.cbrake_mode()
        terminal.clear()

        rows: int = cursor.move_cursor_to_bottom()

        messages: MessageStore = MessageStore(redraw_output, rows - 1)

        await messages.append('Enter numeric value <q to quit>')

        stdin_reader = await create_stdin_reader()

        while True:
            line = await read_line(stdin_reader, messages)

            if line.lower() in ('q', 'quit', 'quit()'):
                break

            try:
                delay = int(line)
                asyncio.create_task(sleeper(delay, messages))
            except ValueError:
                await messages.append('[ERROR] Use numeric values <q to quit>')

    finally:
        terminal.restore_terminal_state(old_terminal)


if __name__ == '__main__':
    asyncio.run(main())
