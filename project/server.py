import sys
import time
from socket import *
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-a', '--address', required=True, dest='address', help='server.py -a <address> [-p <port>]')
parser.add_argument('-p', '--port', required=False, dest='port')
args = parser.parse_args()

address = args.address
port = int(args.port) if args.port != None else 7777

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


