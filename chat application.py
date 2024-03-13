//server code//
import socket

HOST = ''  # Listen on all available interfaces
PORT = 54

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Server listening on port {PORT}...")

    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Received message from client: {message}")
            if message == "bye":
                break
            reply_message = input("Enter your reply message: ")
            conn.sendall(reply_message.encode())

print("Server connection closed")


