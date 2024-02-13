import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12211))  # Устанавливаем соединение с сервером

while True:
    text = input("Что отправить на сервер?  ")

    client_socket.sendall(text.encode('utf-8'))  # Отправляем данные на сервер

    data = client_socket.recv(1024)  # Получаем ответ от сервера

    print(f"Сервер отправил данные: {data.decode()}")
    exit = int(input("0/1: "))
    if exit == 0:
        break
client_socket.close()  # Закрываем соединение