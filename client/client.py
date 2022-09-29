import socket
import time

HOST, PORT = "localhost", 9999
data = "Hey Arunachala:whatsup man "

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    while 1:
        sock.sendall(bytes(data + "\n", "utf-8"))
        print("Sent:     {}".format(data))
        received = str(sock.recv(1024), "utf-8")
        print("Received: {}".format(received))

        time.sleep(1000)
        exit(0)



z00