import socket
import sys

PATH = "/Users/rjabbala/Projects /Event_Processing/BillionEventsPerOneHour/tests/testinputBevents.txt"
HOST, PORT = "localhost", 9999
data = "Hey Arunachala:whatsup man "

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        file = open(PATH)
        lineList = file.readlines()
        map(lambda x: x.string.strip(), lineList)
        for line in lineList:
            sock.send(bytes(line, "utf-8"))
    file.close()

''' count=0
        for line in lineList:
            sock.send(bytes(line, "utf-8"))
            count = count + 1
            if count == 10:
                break'''