
def generateEvents():
    totalEvents = 999999
    procMsges   = 0
    with open('testinputBevents.txt','a') as file:
         while totalEvents >= 0 :
               mesg = 'msg'+str(procMsges)+'\n'
               file.writelines(mesg)
               totalEvents -= 1  
               procMsges += 1
         file.close()

if __name__ == '__main__':
   generateEvents()
