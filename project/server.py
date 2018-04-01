import sys
import json
from socket import *
from argparse import ArgumentParser

#ф-я преобразования цельсия в фаренгейт по заданным параметрам
def cel_to_far_convert(options):
    result = {}
    min = options['min']
    max = options['max']
    step = options['step']

    for с in range(min,max,step):
        f = (с * 1.8) + 32
        result[с] = float('{:.1f}'.format(f))

    return result


parser = ArgumentParser()
parser.add_argument('-a', '--address', required=True, dest='address', help='server.py -a <address> [-p <port>]')
parser.add_argument('-p', '--port', required=False, dest='port')
args = parser.parse_args()

address = args.address
port = int(args.port) if args.port != None else 7777

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((address, port))
server_socket.listen(5)

while True:
    client, address = server_socket.accept()
    print("Получен запрос от клиента %s" % str(address))

    recive_buf = client.recv(1024)          # принимаем 1024 байта
    json_buf = recive_buf.decode("utf-8")   # декодируем полученную информацию
    client_options = json.loads(json_buf)   # десереализация

    result = cel_to_far_convert(client_options)

    server_answer = json.dumps(result)      # сереализация
    buf = server_answer.encode()            # кодировка
    client.send(buf)                        # оптаврялем ответ

    client.close()


