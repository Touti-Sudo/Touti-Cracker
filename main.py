import platform
import subprocess
import os
import time
import sys
from scripts.dependencies_install_script import mac_install, check_and_install_dependencies
from scripts.ip_script import get_private_ip
from scripts.clear_cmd_script import clearsystem
from scripts.antivirus_check_script import is_av_active
from scripts.type_writer_script import typewriter
from scripts.admin_check_script import is_admin
from scripts.registers_saving_script import save_registers
from scripts.ipv4_script import get_public_ip
from scripts.password_generator_script import generate_passwords
from scripts.cracking_script import cracker
from scripts.wifi_cracking_script import automated_wifi_attack
from scripts.payload_generation_script import payload_script
def main():
    systemtype = platform.system()
    user = os.getlogin()
    mac_install()
    check_and_install_dependencies()

    try:
        import csv
        import secrets
        import pyfiglet
        import signal
        import requests
        import webbrowser
        import socket
        from rich.console import Console
        from rich.panel import Panel
        from rich.text import Text
        from unit.neon_module import neon_text

        console = Console()
        from colorama import init, Fore, Back, Style
        import ctypes
    except ImportError as e:
        print(f"Error: {e}. Please install the required modules using:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    init()

    ip = get_private_ip()

    clearsystem(OS=systemtype)


    try:
        info = Fore.BLUE + "[Info]:" + Style.RESET_ALL
        warning = Fore.MAGENTA + "[Warning]:" + Style.RESET_ALL
        disclamer = Fore.YELLOW + "[Disclamer]:" + Style.RESET_ALL
        error = Fore.RED + "[Error]:" + Style.RESET_ALL
        inputs = Fore.GREEN + "[Input]:" + Style.RESET_ALL
        first = Fore.RED + " [1]" + Style.RESET_ALL
        second = Fore.RED + " [2]" + Style.RESET_ALL
        third = Fore.RED + " [3]" + Style.RESET_ALL
        fourth = Fore.RED + " [4]" + Style.RESET_ALL
        fifth = Fore.RED + " [5]" + Style.RESET_ALL
        sixth = Fore.RED + " [6]" + Style.RESET_ALL
        seventh = Fore.RED + " [7]" + Style.RESET_ALL
        eigth = Fore.RED + " [8]" + Style.RESET_ALL
        nine = Fore.YELLOW + " [99]" + Style.RESET_ALL
        the_link = "https://github.com/Touti-Sudo"
        creator = Fore.RED + " Created by ----> Touti-Sudo : " + the_link + Style.RESET_ALL
        gui = (
            Fore.LIGHTRED_EX
            + pyfiglet.figlet_format("Touti Cracker" + " v2.2.2", font="slant")
            + Style.RESET_ALL
        )
        gui2 = gui + "                                        " + creator + "\n"
        typewriter(gui2, 0.01)
        neon_color = "#FFFF00"
        texte = "🔥 Welcome to Touti Cracker 🔥\nUse responsibly!"
        console.print(
            Panel(
                f"[bold cyan]{texte}[/bold cyan]",
                title=f"[bold {neon_color}]Touti Cracker[/bold {neon_color}]",
                border_style=f"bold {neon_color}",
            )
        )
        print("\n")

        infos = (
            info
            + "Welcome to Touti Cracker This tool will allow you to hack anyone password."
        )
        typewriter(infos, 0.01)
        infos = (
            warning
            + "This is for educational purposes only , i am not responsible for any bad and suspicious activities.Thank you for considering my words !!"
        )
        typewriter(infos, 0.01)
        infos = (
            disclamer
            + "This is a beta version of Touti Cracker and it may contain bugs or errors, please report them on my github page: "
            + the_link
            + " and i will fix them as soon as possible !"
        )
        typewriter(infos, 0.01)
        if not is_admin(OS=systemtype):  
            print("\n" + warning + "Run as Administrator!")
            if systemtype == "Windows":
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, " ".join(sys.argv), None, 1
                )
                sys.exit()
            elif systemtype == "Linux":
                print(warning + "Please run the script with sudo.")
                sys.exit()
            elif systemtype == "Darwin":
                print(warning + "Please run the script with sudo.")
                sys.exit()
        else:
            print("\n" + info + "You are running as Administrator!")

        if is_av_active(): 
            print(
                warning
                + "Antivirus may block the Password Cracking process. Temporarily disable it."
            )
        else:
            print(info + "Antivirus is disabled.")
        print("\n")

        versionpy = platform.python_version()
        finalversion=f'Python{versionpy[:-1].replace(".", "")}'
        print(finalversion)
        printpy = info + "you are running on " + finalversion + "\n"

        while True:
            neon_shades = ["#00FFFF", "#00DDFF", "#00BBFF", "#0099FF", "#0077FF", "#0055FF"]

            menu_text = [
                "[1] Password Generator",
                "[2] Brute Force",
                "[3] Steal Local Target Registers",
                "[4] Crack a Wifi Password",
                "[5] Reverse Shell Payload",
                "[6] launch msfconsole",
                "[7] View Github Page",
                "[8] View README.txt",
                "[9] View License",
                "[99] Exit",
            ]
            styled_text = Text()
            for i, line in enumerate(menu_text):
                color = neon_shades[i % len(neon_shades)]
                styled_text.append(line, style=f"bold {color}")
                styled_text.append("\n")

            console.print(Panel(styled_text, title="🔹 Menu 🔹", border_style="cyan"))

            choice = input(inputs + "Please choose an option:")
            if choice == "99":
                print(info + "Exiting...")
                clearsystem(OS=systemtype)
                neon_text("Good Bye", duration=3)
                print("Thank's for using Touti-Sudo's Software")
                break
            elif choice == "2":
                cracker(inputs=inputs,OS=systemtype,user=user,info=info,error=error,warning=warning,the_link=the_link,versionpy=finalversion,disclamer=disclamer)

            elif choice == "1":
                generate_passwords(info=info, first=first, second=second, inputs=inputs, OS=systemtype, user=user, error=error)

            elif choice == "7":
                webbrowser.open(the_link)

            elif choice == "8":
                print(info + "Opening README.txt...")
                the_link2 = (
                    "https://github.com/Touti-Sudo/Touti-Cracker/blob/main/README.md"
                )
                webbrowser.open(the_link2)

            elif choice == "3":
                save_registers(OS=systemtype,user=user,info=info,error=error,the_link=the_link,inputs=inputs)
                print(
                    info + "You can now bruteforce the password using the saved registers"
                )
            elif choice == "6":
                if systemtype == "Windows":
                    print(info + "Launching msfconsole...")
                    subprocess.run("msfconsole", shell=True, text=True)
                elif systemtype == "Linux":
                    print(info + "Launching msfconsole...")
                    subprocess.run("msfconsole", shell=True, text=True)
                elif systemtype == "Darwin":
                    print(info + "Launching msfconsole...")
                    subprocess.run("msfconsole", shell=True, text=True)

            elif choice == "4":
                if systemtype == "Windows":
                    print(
                        info
                        + "The cracking process on Windows is limited to the GUI version of aircrack-ng due to the lack of support for the CLI version on Windows."
                    )
                    time.sleep(10)
                    subprocess.run('"Aircrack-ng GUI.exe"', shell=True, text=True)
                elif systemtype == "Linux" or systemtype == "Darwin":
                    print(info + first + " Automatically")
                    print(
                        info
                        + second
                        + " Manually(Creates a Terminal Window where you can launch aircrack-ng commands)"
                    )
                    choice = input(inputs + "Please choose an option: ")
                    if choice == "1":
                        automated_wifi_attack(OS=systemtype,user=user)
                    elif choice == "2":
                        subprocess.run(
                            "bash  -c 'aircrack-ng; exec bash'", shell=True, text=True
                        )
                    else:
                        print(error + "Please enter a valid choice (1/2).")
            elif choice == "9":
                webbrowser.open(
                    "https://github.com/Touti-Sudo/Touti-Cracker/blob/main/LICENSE.txt"
                )
            elif choice == "5":
                payload_script(OS=systemtype,error=error,first=first,info=info,inputs=inputs,second=second,the_link=the_link,user=user,warning=warning,ip=ip)
            else:
                print(error + "Please enter a valid choice (1/2/3/4/5/6/99).")

    except KeyboardInterrupt:
        print(f"\n{error}  Program interrupted. Exiting...")
        clearsystem(OS=systemtype)
        neon_text("Good Bye", duration=3)
        print("Thank's for using Touti-Sudo's Software")
        exit()

    except ValueError as e:
        print(error + f" {e}")
        exit()
    except PermissionError:
        print(
            error + "Please run Touti Cracker at admin mod! and disable antivirus software"
        )
        exit()
    except FileNotFoundError as e:
        print(f"{error}  The file was not found. Try reinstalling Touti Cracker !   {e}")
        exit()
    except OSError:
        print(error + "Please check your system compatibility and stability")
        exit()
if __name__ == "__main__":
    main()  
