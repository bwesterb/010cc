import zmq
import time
import random

class Client(object):
    def main(self):
        identifier = random.randint(0,10000000)
        zctx = zmq.Context()
        s = zctx.socket(zmq.REQ)
        s.connect('tcp://localhost:5555')
        print 'request for next batch'
        while True:
            s.send_json(['ping', identifier])
            print s.recv_json()
            time.sleep(1)


if __name__ == '__main__':
    Client().main()
