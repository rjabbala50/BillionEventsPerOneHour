
import os

 #max connections are tested in Int32 bit machine
 #max parallel are 2^32-1 = 65536 ( 32 bit machines)
MaxParallelConnections32Bit = lambda x: 'os.system(x)'

MaxParallelConnections32Bit('python3 client')