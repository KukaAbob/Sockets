import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
a = 123
print('0987666545321aAAAA')
s.bind(( '0.0.0.0',8000))
message = s.recv(128)
print (message)
s.listen(2)
s.send('bbb')
