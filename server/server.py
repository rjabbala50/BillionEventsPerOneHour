import socket
import socketserver
import sys
import time

start_time = time.time()
end_time = time.time()
HOST, PORT = "localhost", 9999

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        start_time = time.time()
        socketfile = self.request.makefile()
        while 1:
            data = socketfile.readline()
            if not data:
                break
            else:
                print(data.strip())
        end_time = time.time()
        print("Server - Execution Time: ", (end_time - start_time))

if __name__ == "__main__":
    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

