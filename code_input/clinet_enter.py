import socket
def start(code, lang):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Подключаемся :3
    client_socket.connect(('127.0.0.1', 11221))
    # Отправляем код, надо еще чтение допилить, но это потом)
    mess = f"{lang}-{code}"
    client_socket.sendall(mess.encode('utf-8'))
    
    # Закрываем, больше нам нечего не нужно, пока что... Конечно еще нужно будет получать
    # от сервера, что то вроде результата итерпритации или компиляции, думаю будет около 4-х
    # языков программирование python, rust, c\c++
    
    client_socket.close()