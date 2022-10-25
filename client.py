import socket
s=socket.socket()
s.connect(("DESKTOP-9FOJ24A",51756))
while True:
    msg1=input("to server:")
    msg2=msg1.encode("utf-8")
    s.send(msg2)
    msg3=s.recv(100)
    msg4=msg3.decode("utf-8")
    print("from server: ",msg4)