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
        print('Coudnt open the file', PATH)
        sys.exit(1)
    return file

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        file = get_file_stream()
        message = file.read()
        sock.send(bytes(message, "utf-8")),
        #print ("Bytes: ",len(lines))
        #print("Sent:     {}".format(lines)),
