import socket 
import sys
from thread import *


class Automan_agent(object):
    """
    docstring for Automan_Client
    """
    def __init__(self):
        '''
        constructor
        '''
    
        pass
    def socket_server(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            sys.stderr.write("[ERROR] %s\n" % msg[1])
            sys.exit(1)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #sock.bind((Host,Port))
        #sock.bind(('10.90.1.132', 54321))
        sock.bind(('127.0.0.1', 10000))
        sock.listen(5)
        print "Socket create succeed!!"
        print "Server is Listening"
        while True:
            (csock, adr) = sock.accept()
            print "Client Info: ", csock, adr 
            start_new_thread(automan.threadwork, (csock,))
        sock.close()
                
    def threadwork(self, client):
        #Sending message to connected client
        #client.send("Welcome to the server.\n") 
        #infinite loop so that function do not terminate and thread do not end.
        msg = client.recv(1024)
        if not msg:
            pass
        else:
            print "Client send: " + msg    
            result = automan.call_function(msg)
            client.sendall(msg)
        client.close()
    
    #add abby code
    def call_function(self, msg):        
        keys = msg
        items = keys.split(',')     # items[0]=.py file name, items[1]=.py class name, items[2]=.py function name
        parameter = str(','.join(items[3:]))
        exec('from automan.util.' + items[0] + ' import ' + items[1]) 
        ob = eval(items[1]+'()')
        defname = items[2] + '("' + parameter + '")'
        def_result = eval('ob.'+ defname)
        print def_result
        return def_result


if __name__ == '__main__':

    automan = Automan_agent()
    automan.socket_server()