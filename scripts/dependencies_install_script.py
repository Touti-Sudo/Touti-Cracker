import os
import platform
import sys
import requests
import subprocess
import time
import winreg


systemtype = platform.system()

def is_metasploit_installed():
    uninstall_keys = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    for root in (winreg.HKEY_LOCAL_MACHINE,):
        for key_path in uninstall_keys:
            try:
                with winreg.OpenKey(root, key_path) as key:
                    for i in range(winreg.QueryInfoKey(key)[0]):
                        subkey_name = winreg.EnumKey(key, i)
                        with winreg.OpenKey(key, subkey_name) as subkey:
                            try:
                                name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                if "Metasploit" in name:
                                    return True
                            except FileNotFoundError:
                                continue
            except FileNotFoundError:
                continue
    return False
def mac_install():
    info = "[Info]: "
    if systemtype != "Darwin":
        return

    print(info + "Installing important dependencies for macOS...")

    commands = [
        "brew install python",
        "brew install libffi",
        "brew install openssl",
        "python3 -m venv impacket-env",
        "impacket-env/bin/python -m pip install --upgrade pip",
        "impacket-env/bin/python -m pip install impacket requests",
    ]

    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)


def aircrack_download(user, info="[Info]: ", error="[Error]: "):
    print(info + "Downloading aircrack-ng...")
    aircrack_url = r"https://download.aircrack-ng.org/aircrack-ng-1.7-win.zip"
    aircrack_path = os.path.join("C:\\Users", user, "aircrack")
    os.makedirs(aircrack_path, exist_ok=True)
    zip_file = os.path.join(aircrack_path, "aircrack-ng.zip")

    response = requests.get(aircrack_url, stream=True)
    if response.status_code == 200:
        with open(zip_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(info + "Aircrack-ng downloaded successfully.")
    else:
        print(error + "Failed to download aircrack-ng.")
        time.sleep(5)


def check_and_install_dependencies():
    error = "[Error]: "
    info = "[Info]: "
    warning = "[Warning]: "
    user = os.getlogin()
    systemtype = platform.system()

    try:
        print(info + "Checking and installing dependencies...")

        response = requests.get(
            "https://raw.githubusercontent.com/Touti-Sudo/Touti-Cracker/main/requirements.txt"
        )
        with open("requirements.txt", "wb") as file:
            file.write(response.content)

        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--upgrade",
                "pip",
                "setuptools",
                "wheel",
            ],
            check=True,
        )
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
        )

        print(info + "Dependencies checked and installed successfully.")

        if systemtype == "Windows":

            seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"
            if not os.path.exists(seven_zip_path):
                print(
                    error
                    + "7-Zip is not installed. Please install it from https://www.7-zip.org/"
                )
                time.sleep(5)
                return

            aircrack_zip = rf"C:\Users\{user}\aircrack\aircrack-ng.zip"
            if not os.path.exists(aircrack_zip):
                aircrack_download(user, info, error)

            aircrack_path = os.path.join("C:\\Users", user, "aircrack")
            extract_path = os.path.join(aircrack_path, "extracted")
            bin_path = os.path.join(extract_path, "aircrack-ng-1.7-win", "bin")
            os.makedirs(bin_path, exist_ok=True)

            print(info + "Unzipping Aircrack-ng...")
            command = rf'"{seven_zip_path}" x "{aircrack_zip}" -o"{extract_path}" -y'
            subprocess.run(command, shell=True, text=True, check=True)

            path_to_add = rf"{bin_path}"
            subprocess.run(f'setx PATH "%PATH%;{path_to_add}"', shell=True, text=True)
            print(info + "Aircrack-ng path added to system PATH successfully.")

            metasploit_dir = rf"C:\Users\{user}\metasploit"
            metasploit_url = (
                "https://windows.metasploit.com/metasploitframework-latest.msi"
            )
            installer_path = os.path.join(metasploit_dir, "metasploit.msi")
            installed_check = (
                r"C:\Program Files\Metasploit\Framework\bin\msfconsole.bat"
            )

            if not os.path.exists(installer_path):
                print(info + "Downloading Metasploit...")
                os.makedirs(metasploit_dir, exist_ok=True)
                response = requests.get(metasploit_url, stream=True)
                response.raise_for_status()
                with open(installer_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(info + "Metasploit downloaded successfully.")
            else:
                print(info + "Metasploit installer already exists.")

            if systemtype == "Windows":

                if is_metasploit_installed():
                    print(info + "Metasploit is already installed (registry check).")
                else:
                    print(info + "Launching Metasploit installer...")
                    subprocess.run(
                        ["msiexec", "/i", installer_path],
                        check=True
                    )
            subprocess.run("choco install hashcat ")
            

        elif systemtype == "Linux":
            subprocess.run("sudo apt-get update", shell=True)
            subprocess.run(
                "sudo apt-get install -y aircrack-ng metasploit-framework hashcat",
                shell=True,
            )

        elif systemtype == "Darwin":
            subprocess.run("brew install aircrack-ng metasploit hashcat", shell=True)

        else:
            print(error + f"Unsupported system type: {systemtype}")

    except Exception as e:
        print(error + f"Failed to check and install dependencies: {e}")
