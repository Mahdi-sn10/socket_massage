import socket

HOST = "127.0.0.1" #set local host
# Host = "" #for any host
PORT = 8001
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept()
    #conn : new socket
    # addr : new socket address

    with conn:
        print(f"connect by {addr}")
        while True:
            data = conn.recv(1024)
            if data.decode("utf-8")=="q":
                break
            print(f"{data.decode("utf-8")}")
            massage = input("type any thin:  ")
            conn.sendall(bytes(massage,encoding='utf8'))
