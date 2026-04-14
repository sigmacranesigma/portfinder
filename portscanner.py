import socket

targetip = input("What IP are we looking at? ")
first = True
for port in range(65536):
    s = socket.socket()
    s.settimeout(0.0000001)

    result = s.connect_ex((targetip, port))

    if result == 0:
        if first == True:
            with open(r"C:\Users\abryant\Downloads\portscan.txt", "w") as f:
                f.write(f"Port {port} is open")
            first = False
        else:
            with open(r"C:\Users\abryant\Downloads\portscan.txt", "a") as f:
                f.write(f"\nPort {port} is open")
    print(port)
    s.close()

