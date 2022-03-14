import asyncio
from telethon import TelegramClient
from telethon.tl import functions, types

with open('anothertoken.txt', 'r') as f:
    TOKEN = f.read()

with open('api.txt', 'r') as api:
    api_id = api.read()

with open('api-hash.txt', 'r') as apih:
    api_hash = apih.read()


client = TelegramClient('Minh', api_id, api_hash)
client.start()

async def main():
    channel = await client.get_entity('HYPERPC')
    messages = await client.get_messages(channel, limit= None) #pass your own args

    #then if you want to get all the messages text
    for x in messages:
        print(x.text) #return message.text


loop = asyncio.get_event_loop()
loop.run_until_complete(main())