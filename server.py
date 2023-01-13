import socket

sock = socket.socket()
print(f"i. Запуск сервера;")
sock.bind(('', 2203))
print(f"ii. Начало прослушивания порта;")
sock.listen(2)
print(f"iii. Подключение клиента;")
conn, addr = sock.accept()

print(addr)

msg = ''
while True:
    print(f"iv. Прием данных от клиета;")
    data = conn.recv(1024)
    if not data:
        print(f"vi. Отключение клиента;")
        break
    msg += data.decode()
    print(f"v. Отправка данных клиенту;")
    conn.sendall(data)

print(msg)

conn.close()
print(f"vii. Остановка сервера;")