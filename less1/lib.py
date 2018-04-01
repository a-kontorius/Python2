import json

def main_loop_for_server(sock):
    prog = \
        {
            "+" : (10,20),
            "-" : (50,30),
            "*" : (5,7),
            "/" : (5,3)
        }
    prog_json = json.dumps(prog)
    buf = prog_json.encode()

    sock.send(buf)
    result_buf = sock.recv(1024)

    result_json = result_buf.decode()
    result = json.loads(result_json)

    return result


##################################################
def main_loop_for_client(sock):
    buf = sock.recv(1024)
    buf_json = buf.decode()
    prog = json.loads(buf_json)
    result = {}

    func = \
        {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": div
        }

    for op in prog:
        result[op] = func[op](prog[op][0], prog[op][1])

    result_json = json.dumps(result)
    result_buf = result_json.encode()
    sock.send(result_buf)

def div(x, y):
    return x / y