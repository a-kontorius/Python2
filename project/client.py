import sys
import json
from socket import *

if len(sys.argv) < 2:
    print("Неверно заданы параметры запуска: server.py <address> [:port]")
    sys.exit(1)

address = sys.argv[1]
port = int(sys.argv[2]) if len(sys.argv) == 3 else 7777

param = {
    "min": 10,
    "max": 53,
    "step": 3
}
json_param = json.dumps(param)
buf = json_param.encode("utf-8")


client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((address, port))
client_socket.send(buf)

answer_buf = client_socket.recv(1024)
json_buf = answer_buf.decode("utf-8")
answer = json.loads(json_buf)
print(answer)
client_socket.close()



