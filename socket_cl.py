import socket

HOST = "127.0.0.1"
PORT = 8001
with  socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    massage = input("type any thin:  ")
    s.sendall(bytes(massage,encoding='utf8'))
    data = s.recv(1024)
    
print(f"Receve {data.decode("utf-8")}")