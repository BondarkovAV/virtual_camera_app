from socket import socket
import time
import asyncio


class ConnectSocket:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.s = socket()

    async def connect(self) -> tuple[socket, str]:
        self.s.bind((self.host, self.port))
        self.s.listen()
        self.s.setblocking(False)
        con, addr = await self.accept_cycle()
        addr_string = f"Подключено {addr}"
        return con, addr_string

    async def accept_cycle(self):
        loop = asyncio.get_event_loop()
        while True:
            con, addr = await loop.sock_accept(self.s)
            if con:
                return con, addr
