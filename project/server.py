import sys
import time
from socket import *


if len(sys.argv) < 2:
    print("Неверно заданы параметры запуска: server.py <address> [:port]")
    sys.exit(1)


address = sys.argv[1]
port = int(sys.argv[2]) if len(sys.argv) == 3 else 3333

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((address, port))
server_socket.listen(5)

print("Сервер запущен на адресе '{0}' и порту {1}".format(address,port))

while True:
    client, address = server_socket.accept()
    print("Получен запрос от клиента %s" % str(address))
    timestr = time.ctime(time.time()) + "\n"
    client.send(timestr.encode('ascii'))
    client.close()


