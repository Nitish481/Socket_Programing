import socket
TCP_PORT = 32768
IP_ADDR = '192.168.0.4'
BUF_SIZE = 1024
k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
k.connect((IP_ADDR,TCP_PORT))
print("Client sent connection request")
k.send("sudo rm rf".encode())
data = k.recv(BUF_SIZE)
print(data.decode())
k.close()