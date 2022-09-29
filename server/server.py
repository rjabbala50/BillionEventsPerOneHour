import socketserver

HOST, PORT = "localhost", 9999

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        while 1:
            data = self.rfile.readline().strip()
            # print("{} wrote:".format(self.client_address[0]))
            print(data)
            # self.wfile.write(self.data.upper())

if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
