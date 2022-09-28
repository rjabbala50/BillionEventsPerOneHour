
import socket

def client_program():
    host = socket.gethostname()
    port = 9000 

    client_socket = socket.socket() 
    client_socket.connect((host, port)) 

    message = ' '
    with open('../tests/testinputBevents.txt', 'r') as file:
         while message.lower().strip() != 'bye':
               for line in file:
                   client_socket.send(line.encode())  
        #data = client_socket.recv(1024).decode()'''
        #print('Received from server: ' + data)  # show in terminal'''
#              message = input(" -> ") 

    client_socket.close()
    file.close()  

if __name__ == '__main__':
    client_program()
