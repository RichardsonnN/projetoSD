import socket
import threading
import random

client = socket.scoekt(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("localhost", random.randint(8000, 90000)))

name = input("nickname: ")
def receive():
  while True:
    try:
      message, _ = client.recvfrom(1024)
      print(message.decode())
    except:
      pass
t = threading.Thread(target=receive)
t.start()

client.send(f"SIGNUP_TAG: {name}".encode(), ("localhost", 9999))

while True:
  message = input('')
  if message == "!q":
    exit()
  else:
    client.sendto(f"{name}: {message}". encode(), ("localhost", 9999) )




