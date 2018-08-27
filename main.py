import asyncio
import aiomcache
from uuid import uuid4


uuids = []
for i in range(1,pow(10,4)):
    uuids.append(str(uuid4()).encode('utf-8'))


loop = asyncio.get_event_loop()

async def main():
    mc = aiomcache.Client("127.0.0.1", 11211, loop=loop)
    futures = []
    for i in range(1,pow(10,5)):
        futures.append(mc.set(str(i).encode('utf-8'), uuids[i % len(uuids)]))
    for f in futures:
        await f

loop.run_until_complete(main())
