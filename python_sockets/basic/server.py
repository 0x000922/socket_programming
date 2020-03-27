import socket
seversock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
seversock.bind(('localhost',8080))
seversock.listen(5)
sock , addr = seversock.accept()
msg = ''
while True:
    #sock.send(bytes("chat","utf-8"))
    msg = sock.recv(1024)
    print(repr(msg))
    msg = input("you->")
    sock.send(bytes(msg,"utf-8"))
