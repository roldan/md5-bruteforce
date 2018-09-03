#!/usr/bin/env python
# md5brute.py

import sys,Queue,threading,hashlib,os

NumOfThreads=100  # Number of threads
queue = Queue.Queue()

# get hash and wordlist input
try:
    TargetHash=sys.argv[1].lower()
    WordList=open(sys.argv[2],'r')
except:
    print "Usage: %s hash wordlist" % sys.argv[0]
    sys.exit(1)

class checkHash(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue
    def run(self):
        while True:
            self.clear=self.queue.get()
            if hashlib.md5(self.clear).hexdigest() == TargetHash:
                print "Hash found!!! %s = %s" % (self.clear,TargetHash)
                os._exit(0)
            self.queue.task_done()

#spawn a pool of threads
for i in range(NumOfThreads):
    t=checkHash(queue)
    t.setDaemon(True)
    t.start()

#populate queue with wordlist
for word in WordList.readlines():
    queue.put(word.strip())

queue.join()
