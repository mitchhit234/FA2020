from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready")
while True:
  message, clientAddress = serverSocket.recvfrom(2048)
  modifedMessage = message.decode.upper()
  serverSocket.sendto(modifedMessage.encode(), clientAddress)