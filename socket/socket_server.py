# ====================================================================================================
# SOCKETS
# ====================================================================================================
import socket
import errno

# Questions when working with sockets:
# 1. Internet or unix socket? internet
# 2. What kind of protocol are we using, tcp or udp? tcp(SOCK_STREAM) is connection oriented (it is slower), udp(SOCK_DGRAM) is faster (you have the risk of losing data)
# 3. Which ip do we want to host the server on?
# 4. Which port do we want to use?

host = '127.0.0.1'
port = 55556
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        s.bind((host, port))
        print('Bound! Host: {}, Port: {}'.format(host, port))
        s.listen()

        while True:
            client, address = s.accept()
            print('Conneted to {}'.format(address))
            client.send("You are connected!".encode())
            client.close()
    except OSError as e:
        print("errno:", e.errno, "str:", e)
        if e.errno == errno.EADDRNOTAVAIL:
            print(
                "Address not available: check your interfaces or use 127.0.0.1 or 0.0.0.0")
