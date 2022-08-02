import socket
from random import randint
import sys
import pickle
from time import sleep
trans=0
f = open('sample.txt','r')
seq=0
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 2345
sock.bind(('',port))
sock.listen(2)
conn,addr = sock.accept()
print('connection recieved from :',addr)
msg = f.read(512)

while msg:
    data = [seq,msg]
    dat = pickle.dumps(data)
    conn.send(dat)
    print('sent package: ',seq)
    rep = conn.recv(512)
    if seq == 1:
        print('recevied ack for packet no:',seq)
        seq =0
    elif seq == 0:
        print('received ack for packet no:',seq)
        seq =1
    msg = f.read(512)

print("All Packets sent sucessfully !!")
f.close()
conn.close()
sock.close()
















             
