import asyncio
import sys
from collections import deque

from editors import remove_char
from cursor_controls import Cursor
from storages import MessageStore


async def read_line(
    stdin_reader: asyncio.StreamReader,
    message_store: MessageStore
) -> str:
    """Cчитывает в буффер по одному ascii символу за раз,
    пока не встретит перевод коретки (ввод Enter).
    Отслеживается нажатие клавиши Delete."""
    delete_key: bytes = b'\x7f'
    buffer: deque = deque()
    flag: bool = True

    while (char := await stdin_reader.read(1)) != b'\n':
        if char == delete_key and buffer:
            buffer.pop()
            remove_char()
            flag = not flag
        else:
            try:
                sys.stdout.write(char.decode())
            except UnicodeDecodeError:
                if flag:
                    error_message: str = (
                        '[ERROR] \'utf-8\' codec can\'t decode input byte. '
                        'Use ASCII chars instead <q to quit>'
                    )
                    await message_store.append(error_message)
                    flag = not flag
                continue

            buffer.append(char)

        sys.stdout.flush()

    Cursor.clear_line()
    return b''.join(buffer).decode()


async def create_stdin_reader() -> asyncio.StreamReader:
    """Создает поток чтения данных."""
    stream_reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(stream_reader)
    loop = asyncio.get_running_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    return stream_reader
