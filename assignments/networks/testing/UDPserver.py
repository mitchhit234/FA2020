from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready")
while True:
  message, clientAddress = serverSocket.recvfrom(2048)
  recieved_string = message.decode().upper()
  print("Recieved string: " + recieved_string)
  counter = 0
  for i in recieved_string:
    counter += 1
  print(counter)
  serverSocket.sendto(bytes(counter), clientAddress)