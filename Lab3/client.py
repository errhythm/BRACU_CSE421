import socket

HEADER=16
PORT=5050

# IP Address of the server
CLIENTSERVER=socket.gethostbyname(socket.gethostname())

# Bind the address
ADDR=(CLIENTSERVER, PORT)
FORMAT="utf8"

# Will disconnect if typed "End"
DISCONNECT_MSG="End"

# Generating the server
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)


def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    # Finding the remaining length
    send_length+=b' '*(HEADER-len(send_length))
    
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    

#Task 1
send(f"Client's IP Address is: {CLIENTSERVER} and Device name is: {socket.gethostname()}")
send(DISCONNECT_MSG)

   