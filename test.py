import asyncio
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

async def run(loop):
    nc = NATS()
    data = {b"name" : b"safi", b"age" : b"39"}

    await nc.connect("localhost:4222", loop=loop)
    await nc.publish("node-sub", data[b'name'])
    await nc.publish("node-sub", b'World')
    await nc.publish("node-sub", b'!!!!!')

    async def help_request(msg):
        print(msg)
    # Terminate connection to NATS.
    await nc.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()
