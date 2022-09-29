import socketserver

HOST, PORT = "localhost", 9999
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
       socketfile = self.request.makefile()
       while 1:
           data = socketfile.readline()
           if not data:
                break
           else:
                print(data.strip())
           # self.wfile.write(self.data.upper())

if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
