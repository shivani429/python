import socket
s=socket.socket()
s.bind(("DESKTOP-9FOJ24A",51756))
s.listen(1)
c,add=s.accept()
while True:
    msg1=c.recv(100)
    msg2=msg1.decode("utf-8")
    print("from client: ",msg2)
    msg3=input("to client:")
    msg4=msg3.encode("utf-8")
    c.send(msg4)