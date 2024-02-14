import socket
import os_assebler

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8172))
#количество не важно
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    try:
        data = client_socket.recv(1024)
        print(f"Клиент отправил код: {data.decode()} ")
        os_assebler.start(data.decode())
    except:
        pass
client_socket.close()
