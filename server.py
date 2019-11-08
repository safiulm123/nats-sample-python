import asyncio
import json
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

async def run(loop):
    nc = NATS()
    data = {
            "TimeStamp":"",
            "Hostname":{
                "IP":"",
                "CPU":"",
                "RAM":"",
                "HDD":""
            },
            "Hostname":{
                "IP":"",
                "CPU":"",
                "RAM":"",
                "HDD":""
            },
}

    await nc.connect("localhost:4222", loop=loop)
    await nc.publish("test", json.dumps(data).encode())

    # Terminate connection to NATS.
    await nc.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()
