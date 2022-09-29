
import socket

def tcpServer():
    host = socket.gethostname()
    port = 9000

    srvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srvSocket.bind((host, port))

    srvSocket.listen(2)
    print('Server is ready to accept  2 client connections')

    client, address = srvSocket.accept()
    print ("Acccepted conn from", address)
    counter =1 
    while 1:
        data = client.recv(1024)
        data = data.decode('UTF-8')
        print(" Received from Client: ",data)
        message = "Hi from Server"
        client.send(message.encode('UTF-8'))
        print("# ",counter)
        counter += 1

    client.close()
if __name__ == '__main__':
    tcpServer()
