import socket
HOST = '127.0.0.1'
PORT = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
print("Server is readt to connect")
server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Data from the client is: {message}")
    communication_socket.send(f"Got your data. Thank you paji".encode('utf-8'))
    communication_socket.close()