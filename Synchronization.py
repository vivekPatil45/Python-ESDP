from threading import *
import time
l = Lock()
def play(name):
    l.acquire()
    for i in range(10):
        print("Batting = ",name)
        time.sleep(1)
    l.release()

t1 = Thread(target=play,args=("MSD",))
t2 = Thread(target=play,args=("Kohli",))
t3 = Thread(target=play,args=("Sachin",))

t1.start()
t2.start()
t3.start()


