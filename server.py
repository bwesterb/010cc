import zmq
import os.path
import kyotocabinet

BITS=100000

class Server(object):
    def __init__(self):
        self.workers = {}
    def open_db(self):
        path = 'db.kch'
        if os.path.exists(path):
            self.db = kyotocabinet.db.open(path, kyotocabinet.DB.OWRITER)
            return
        self.db = kyotocabinet.db.open(path, kyotocabinet.DB.OWRITER |
                                             kyotocabinet.DB.OCREATE)
        for i in xrange(BITS):
            self.db.set('todo-{}'.format(i), None)

    def main(self):
        self.open_db()
        zctx = zmq.Context()
        s = zctx.socket(zmq.REP)
        s.bind('tcp://*:5555')
        while True:
            msg = s.recv_json()
            if not isinstance(msg, list) or not msg:
                s.send_json(['error', 'malformed request'])
                continue
            if msg[0] == 'ping':
                s.send_json(['pong'])
                continue
            s.send_json(['error', 'unknown message'])



if __name__ == '__main__':
    Server().main()
