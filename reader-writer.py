import threading
import time
global_counter = 0
class ReaderWriter():
    def __init__(self):
        self.rd = threading.Lock()  #initializing Locks using Lock class in threading module for reading and wrting
        self.wrt = threading.Lock()  

        self.readCount = 0   #initializing number of reader present

    def reader(self):
        global global_counter
        while True:
            self.rd.acquire()      #wait on read Lock 

            self.readCount+=1       #increase count for reader by 1
            

            if self.readCount == 1: #since reader is present, prevent writing on data
                self.wrt.acquire() #wait on write Lock

            self.rd.release()     #sinal on read Lock

            # print(f"> READER {self.readCount}: value of global counter : ",global_counter,'\n',"-"*20)

            print(f"> READER {self.readCount}: value of global counter : {global_counter}\n--------------------")
            
            self.rd.acquire()   #wait on read Lock 

            self.readCount-=1   #reading performed by reader hence decrementing readercount

            if self.readCount == 0: #if no reader is present allow writer to write the data
                self.wrt.release()  # signal on write semphore, now writer can write

            self.rd.release()      #sinal on read Lock

            time.sleep(1)          

    def writer(self):
        global global_counter
        while True:
            self.wrt.acquire()     #wait on write Lock
            
            # print("> WRITER :")  # write the data
            print(f"> WRITER : global counter updated! \n--------------------")
            global_counter = global_counter + 1
            # print("     global counter updated!")
            # print("-"*20)

            self.wrt.release()      #sinal on write Lock

            time.sleep(1)    

    # def main(self):
        # calling mutliple readers and writers
        # t1 = threading.Thread(target = self.reader) 
        # t1.start()
        # t2 = threading.Thread(target = self.writer) 
        # t2.start()
        # t3 = threading.Thread(target = self.reader) 
        # t3.start()
        # t4 = threading.Thread(target = self.reader) 
        # t4.start()
        # t6 = threading.Thread(target = self.writer) 
        # t6.start()
        # t5 = threading.Thread(target = self.reader) 
        # t5.start()
        

if __name__=="__main__":
    rw = ReaderWriter()

    t1 = threading.Thread(target=rw.reader) 
    t1.start()

    t2 = threading.Thread(target=rw.writer) 
    t2.start()

    t3 = threading.Thread(target=rw.reader) 
    t3.start()

    t4 = threading.Thread(target=rw.writer) 
    t4.start()

    t5 = threading.Thread(target=rw.reader) 
    t5.start()

    t6 = threading.Thread(target=rw.writer) 
    t6.start()

    # c = ReaderWriter()
    # c.main()

    # t1 = threading.Thread(target = self.reader) 
    # t1.start()

    # t2 = threading.Thread(target = self.writer) 
    # t2.start()

    # t3 = threading.Thread(target = self.reader) 
    # t3.start()

    # t4 = threading.Thread(target = self.reader) 
    # t4.start()

    # t5 = threading.Thread(target = self.writer) 
    # t5.start()

    # t6 = threading.Thread(target = self.reader) 
    # t6.start()


    
