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


# Salary Calculating Function
def calculate_salary(hours):
    if hours <= 40:
        salary = hours * 200
    else:
        salary = 8000 + (hours - 40) * 300
    return salary


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
            conn.send(f"Salary is Tk {calculate_salary(int(msg))}.".encode(FORMAT))

conn.close()
