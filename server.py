import zmq

class Server(object):
    def __init__(self):
        self.workers = {}
    def main(self):
        zctx = zmq.Context()
        s = zctx.socket(zmq.REP)
        s.bind('tcp://*:5555')
        while True:
            msg = s.recv_json()
            if not isinstance(msg, list) or not msg:
                s.send_json(['error', 'malformed request'])
                continue
            if msg[0] == 'ping':
                if 
                s.send_json(['pong'])
                continue
            s.send_json(['error', 'unknown message'])



if __name__ == '__main__':
    Server().main()
