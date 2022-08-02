import socket
import pickle
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
seq = 1
port = 2345
sock.connect(('127.0.0.1',port))

f= open('a.txt','w')
msg = sock.recv(1024)
while(msg):
    data = pickle.loads(msg)
    if data[1]=='/':
        print('packet rejected')
        sock.send(b'NACK')
    else:
        print('packet ',data[0],'recieved...')
        f.write(data[1])
        sock.send(b'data[1]')
        print(b'data[0]')

    msg = sock.recv(1024)
f.close()
