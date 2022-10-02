import socket
import socketserver
import sys
import time

start_time = time.time()
end_time = time.time()
HOST, PORT = "localhost", 9999

def get_file_stream():
    PATH = "/Users/rjabbala/Projects /Event_Processing/BillionEventsPerOneHour/tests/testinputBevents.txt"
    try:
        file = open(PATH)
    except:
        print('Coudnt open the file', PATH)
        sys.exit(1)
    return file

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            file = get_file_stream()
            message = file.read(5)
            sock.send(bytes(message, "utf-8")),

            socketfile = self.request.makefile()
            while 1:
                data = socketfile.readline()
                if not data:

                    break
                else:
                    print(data.strip())


if __name__ == "__main__":
    start_time = time.time()
    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
    end_time = time.time()
    print("Server - Execution Time: ", (end_time - start_time))
