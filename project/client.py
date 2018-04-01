import sys
from socket import *

if len(sys.argv) < 2:
    print("Неверно заданы параметры запуска: server.py <address> [:port]")
    sys.exit(1)

address = sys.argv[1]
port = int(sys.argv[2]) if len(sys.argv) == 3 else 3333

client_socket = socket(AF_INET, SOCK_STREAM)

try:
    client_socket.connect((address, port))
    tm = client_socket.recv(1024)
    print("Текущее время: %s" % tm.decode('ascii'))
except ConnectionRefusedError as err:
    print(err.strerror)

client_socket.close()


