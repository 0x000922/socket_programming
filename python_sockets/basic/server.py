import socket
seversock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
seversock.bind(('localhost',8080))
seversock.listen(5)
while True:
    sock , addr = seversock.accept()
    sock.send(bytes("first chat","utf-8"))
