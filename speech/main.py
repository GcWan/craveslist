from send import send_receive
import asyncio

item = asyncio.run(send_receive("ingredients"))
