import socket
s = socket.socket()
print('socket succsfully created')
port = 56789
s.bind(('', port))
print(f'socket binded to port {port}')
s.listen(5)
print('socket is listening')
while True:
    c, addr = s.accept()
    print('got connection from', addr)
    message= ('thank for connrecting')
    c.send(message.encode())
    c.close()
    