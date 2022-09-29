
import socket

def client():
    host = socket.gethostname()
    server_port = 9000

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, server_port))

    counter=1
    while 1:
        message = 'Hey, whatsup bro------- '
        client_socket.send(message.encode('UTF-8'))
        data = client_socket.recv(1024)
        print ('Data sent to server: ', data.decode())
        print ("#",counter)
        counter += 1

    client_socket.close()

'''
    with open('../tests/testinputBevents.txt', 'r') as file:
       for line in file:
           client_socket.send(line.encode('UTF-8'))
           data = client_socket.recv(1024)
           print ('Received from server: ', data.decode())
    file.close()
    client_socket.close()
    '''


if __name__ == '__main__':
    client()
