import socket
import sys
import time

PATH = "/Users/rjabbala/Projects /Event_Processing/BillionEventsPerOneHour/tests/testinputBevents.txt"
HOST, PORT = "localhost", 9999
data = "Hey Arunachala:whatsup man "

def get_file_stream():
    try:
        file = open(PATH)
    except:
        print('Coundnt open the file', PATH)
        sys.exit(1)
    return file

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    while 1:
        file = get_file_stream()
        while 1:   # Read all 1MM lines
            line = file.readline()
            print (line)
            if line:
                sock.send(bytes(line, "utf-8")),
                print("Sent:     {}".format(line)),
                #received = str(sock.recv(1024), "utf-8")
                #print("Received: {}".format(received))
            else:
                break
