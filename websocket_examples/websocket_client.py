import asyncio
import sys
import argparse
from websocket import create_connection

def open_websocket(apikey: str, addresses: str) -> object:
    ws = create_connection('wss://sock.mailsac.com/incoming-messages?key={};addresses={}'.format(apikey, addresses))
    return ws
    
async def main(apikey, addresses):
    ws = open_websocket(apikey, addresses)
    while True:
        print(ws.recv())
        await asyncio.sleep(1)

parser = argparse.ArgumentParser(description='Open websocket on a list of addresses')
parser.add_argument('apikey', type=str, help='Mailsac API key')
parser.add_argument('addresses', type=str, help='Comma seperated string of addresses')
args = parser.parse_args()

asyncio.run(main(args.apikey, args.addresses))
