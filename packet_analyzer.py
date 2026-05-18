import socket

target = input("Enter target website: ")

try:
    ip = socket.gethostbyname(target)

    print(f"\nTarget Website: {target}")
    print(f"Resolved IP Address: {ip}")

except:
    print("Error resolving hostname")
