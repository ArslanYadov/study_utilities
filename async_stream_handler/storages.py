from collections import deque
from typing import Callable, Deque, Awaitable


class MessageStore:
    """Хранилище сообщений на основе двусторонней очереди."""

    def __init__(
        self,
        callback: Callable[[Deque], Awaitable],
        max_size: int
    ) -> None:
        self._callback = callback
        self._queue = deque(maxlen=max_size)

    async def append(self, item) -> None:
        """Добавляем сообщение в очередь."""
        self._queue.append(item)
        await self._callback(self._queue)
