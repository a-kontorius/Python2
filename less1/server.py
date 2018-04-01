import socket
import less1.lib as lib

server_sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0)
server_sock.bind(('127.0.0.1', 7777))
server_sock.listen(5)

while True:
    sock, addr = server_sock.accept()
    result = lib.main_loop_for_server(sock)
    print(result)
    sock.close()