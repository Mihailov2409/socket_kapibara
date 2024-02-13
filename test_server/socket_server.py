import socket
import time

exit = 1
client = 0
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12211))  # Привязываем сокет к IP-адресу и порту
server_socket.listen(5)  # Прослушиваем входящие соединения
 
print("Сервер запущен и ожидает подключений...")

while True:
    client_socket, client_address = server_socket.accept()  # Принимаем соединение
    print(f"Клиент подключился: {client_address}")
    
    try:
        data = client_socket.recv(1024)  # Получаем данные от клиента
        client_socket.sendall("Данные получены".encode('utf-8'))  # Отправляем ответ клиенту
        print(f"Клиент отправил данные: {data.decode()}")
    except:
        pass
client_socket.close() # Закрываем соединение