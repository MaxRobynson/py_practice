""" socket : why of communication betwwen two node or socket t o comnicate which other"""

import socket
import sys

# AF_INET : addresse IPV4, SOCK+STREAM : typ of conection TCP
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket succesfully created')
except socket.error as err:
    print(f'soocket  creation failed with erro {err}!')
    
port = 80

try:
    host_ip = socket.gethostbyname('www.github.com')
except socket.gaierror:
    print('error resolving the host')
    sys.exit()
    
s.connect((host_ip, port))
print(f'socket has succesfully to github connected on port {host_ip}')

#ip = socket.gethostbyname('www.github.com')#print(ip)
