import socket

HOST = 'localhost'
PORT = 2203

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"i. Соединение с сервером;")
    s.connect((HOST, PORT))
    data_in = input()
    print(f"iii. Отправка данных серверу;")
    s.sendall(bytes(data_in, encoding = 'utf-8'))
    print(f"iv. Прием данных от  сервера;")
    data = s.recv(1024)
    print(f"Received {data.decode('utf-8')}")
print("Разрыв соединения с сервером")
