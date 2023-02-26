import socket

HEADER=16
PORT=5050

# IP Address of the server
SERVER=socket.gethostbyname(socket.gethostname())

# Bind the address
ADDR=(SERVER, PORT)
FORMAT="utf8"

# Will disconnect if typed "End"
DISCONNECT_MSG="End"

# Generating the server
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

server.listen()

print("Server is Listening")


conn, addr = server.accept()

connected=True

while connected:
    msg_length=conn.recv(HEADER).decode(FORMAT)
    
    if msg_length:
        msg_length=int(msg_length)
        msg=conn.recv(msg_length).decode(FORMAT)
        
        if msg==DISCONNECT_MSG:
            connected=False
            conn.send("GoodBye").encode(FORMAT)
        else:
            print(msg)
            conn.send("Message Received").encode(FORMAT)
                        
conn.close()
        
