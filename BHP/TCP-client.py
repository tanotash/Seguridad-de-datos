import socket

target_host = "www.google.com"
target_port = 80

#crear un objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conectar al cliente
client.connect((target_host,target_port))

#enviar algun dato
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recibir algun dato
response = client.recv(4096)

print response
