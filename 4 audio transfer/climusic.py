import socket
import sys
import zipfile
import os

host = '192.168.1.31'
port = 1337
k = int(sys.argv[1])
zip_name = 'main.zip'

s = socket.socket()
print('[+] Client socket is created.')

s.connect((host, port))
print('[+] Socket is connected to {}'.format(host))

with zipfile.ZipFile(zip_name, 'w') as file:
	for j in range(1, (k+1)):
		file.write('{}.mp3'.format(j))
		print('[+] {}.mp3 is sent'.format(j))

s.send(zip_name.encode())

f = open(zip_name, 'rb')
l = f.read()
s.sendall(l)

#os.remove(zip_name)
f.close()
s.close()
