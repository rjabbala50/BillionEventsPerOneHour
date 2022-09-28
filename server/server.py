import socket

def server_program():

    host = socket.gethostname()
    port = 9000  

    server_socket = socket.socket()
    server_socket.bind((host, port))  

    server_socket.listen(2)	
    print('Server is ready to accept  2 client connections')
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(999999).decode()
#        if not data:
            # if data is not received break
         #   break
       # print("from connected user: " + str(data))
       # data = input(' -> ')
       # conn.send(data.encode()) 

    conn.close()  

if __name__ == '__main__':
    server_program()
