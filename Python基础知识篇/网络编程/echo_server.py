import socket

HOST = '127.0.0.1'
PORT = 65432

# socket.socket()创建了一个socket对象，并且支持上下文管理器，AF_INET代表ipv4。SOCK_STREAM代表TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # 绑定网络接口
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connnected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
