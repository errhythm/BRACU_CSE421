import socket

HEADER = 16
PORT = 5050

# IP Address of the server
SERVER = socket.gethostbyname(socket.gethostname())

# Bind the address
ADDR = (SERVER, PORT)
FORMAT = "utf8"

# Will disconnect if typed "End"
DISCONNECT_MSG = "End"

# Generating the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

server.listen()

print("Server is Listening")

conn, addr = server.accept()

connected = True

while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)

    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)

        if msg == DISCONNECT_MSG:
            connected = False
            conn.send("GoodBye".encode(FORMAT))
        else:
            # Task 1
            # print(msg)
            # conn.send("Message Received".encode(FORMAT))
            # Task 2
            vowels = "aeiouAEIOU"
            count = 0
            for i in msg:
                if i in vowels:
                    count += 1
            if count == 0:
                conn.send("Not Enough Vowels".encode(FORMAT))
            elif count <= 2:
                conn.send("Enough vowels I guess".encode(FORMAT))
            else:
                conn.send("Too many vowels".encode(FORMAT))

conn.close()
