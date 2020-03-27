import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8080))
while True:
    msg = s.recv(1024)
    print("from server->"+msg.decode("utf-8"))
    msg = input("you->")
    s.send(bytes(msg,"utf-8"))
