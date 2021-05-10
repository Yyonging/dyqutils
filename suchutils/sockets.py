import socket

def free_port():
    free_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    free_socket.bind(('0.0.0.0', 0))
    free_socket.listen(5)
    port = free_socket.getsockname()[1]
    free_socket.close()
    return port

def is_connectable(port: int, host="localhost"):
    socket_ = None
    try:
        socket_ = socket.create_connection((host, port), 1)
        result = True
    except socket.error:
        result = False
    finally:
        if socket_:
            socket_.close()
    return result
