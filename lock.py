import threading
import random
import time


class User(threading.Thread):
    running = True

    def __init__(self, username, right, left):
        threading.Thread.__init__(self)
        self.username = username
        self.left = left
        self.right = right

    def run(self):
        while self.running:
            time.sleep(random.uniform(1, 5))
            print("user %s : READY TO RUN " % self.username)
            self.use()

    def use(self):
        ileft, iright = self.left, self.right
        while self.running:
            ileft.acquire() 
            locked = iright.acquire(False)
            if locked: 
                break
            ileft.release()
        else:
            return
        self.using()
        ileft.release()
        iright.release()

    def using(self):
        print('user %s : START' % self.username)
        time.sleep(random.uniform(1, 7))
        print('user %s : FINISH' % self.username)


def main():
    usb = threading.Lock()
    network = threading.Lock()
    graphic = threading.Lock()
    memory = threading.Lock()

    a = User('A', network, graphic)
    b = User('B', usb, memory)
    c = User('C', memory, graphic)
    d = User('D', network, usb)

    User.running = True

    a.start()
    b.start()
    c.start()
    d.start()

    time.sleep(15)
    print("end of process...")
    User.running = False


if __name__ == "__main__":
    main()




