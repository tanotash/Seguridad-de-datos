import socket

target_host = "127.0.0.1"
target_port = 80

#creando el objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#mandando algun dato 
client.sendto("AAABBBCCC",(target_host,target_port))

#recibiendo algun dato 
data, addr = client.recvfrom(4096)

print data

                        