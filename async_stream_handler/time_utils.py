import asyncio
from storages import MessageStore


async def sleeper(delay: int, message_store: MessageStore) -> None:
    await message_store.append('[INFO] Засыпаю на %d сек.' % delay)
    await asyncio.sleep(delay)
    await message_store.append(
        '[INFO] Сон в течении %d сек. закончился' % delay
    )
