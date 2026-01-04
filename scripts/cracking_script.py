import subprocess

from scripts.password_generator_script import generate_passwords
from scripts.registers_saving_script import save_registers


def cracker(inputs,OS,user,info,error,warning,the_link,versionpy,disclamer,extraction_path2):
            request = (
                input(
                    inputs
                    + "Do you want to crack a password using the last saved wordlist? (y/n): "
                )
                .strip()
                .lower()
            )

            if request == "y":
                if OS == "Windows":
                    chemin_fichier = (
                        "C:\\Users\\" + user + "\\Desktop\\Touti_Cracker\\passwordlist.txt"
                    )
                if OS == "Linux":
                    chemin_fichier = (
                        "/home/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
                    )
                if OS == "Darwin":
                    chemin_fichier = (
                        "/Users/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
                    )

                def remove_spaces(text):
                    return text.replace(" ", "")

                OS_no_spaces = remove_spaces(OS)

                if OS_no_spaces == "Windows":

                    save_registers(OS=OS,user=user,info=info,error=error,the_link=the_link,inputs=inputs)

                    print(info + "Extracting hashes from system and SAM files...")

                    command_for_extracth = (
                        f"python C:\\Users\\{user}\\AppData\\Local\\Programs\\Python\\{versionpy}\\Scripts\\secretsdump.py "
                        f"-sam C:\\Users\\{user}\\Desktop\\Backup\\sam.save "
                        f"-system C:\\Users\\{user}\\Desktop\\Backup\\system.save LOCAL"
                    )

                    resultextract = subprocess.run(
                        command_for_extracth, shell=True, capture_output=True, text=True
                    )
                    print(info + "These are the results:\n" + resultextract.stdout)
                    if (
                        resultextract.stderr.startswith("ERROR:")
                        or resultextract.stdout == ""
                    ):
                        print(error + "\n=== Secretsdump Errors ===")
                        print(resultextract.stderr)

                    yourhash = input(
                        inputs
                        + "Please write the hash that you want to crack (from the results): "
                    )

                   
                    print(info + "Launching Hashcat...")

                    command_lunch_hashcat = (
                        f' hashcat -O -m 1000 "{yourhash}" "{chemin_fichier}"'
                    )
                    command_lunch_hashcats = subprocess.run(
                        command_lunch_hashcat, shell=True, capture_output=True, text=True
                    )
                    print(command_lunch_hashcats.stdout)
                    if command_lunch_hashcats.stderr:
                        print(error + "\n=== Hashcat Errors ===")
                        print(command_lunch_hashcats.stderr)

                elif OS == "Linux":
                    print(
                        disclamer
                        + "You need to have the system.save and sam.save files in the /home/"
                        + user
                        + "/Desktop/Backup directory to extract hashes from them."
                    )
                    command_for_extracth = (
                        f"impacket-secretsdump "
                        f"-sam /home/{user}/Desktop/Backup/sam.save "
                        f"-system /home/{user}/Desktop/Backup/system.save LOCAL"
                    )
                    resultextract = subprocess.run(
                        command_for_extracth, shell=True, capture_output=True, text=True
                    )
                    print(info + "These are the results:\n" + resultextract.stdout)
                    if (
                        resultextract.stderr.startswith("ERROR:")
                        or resultextract.stdout == ""
                    ):
                        print(error + "\n=== Secretsdump Errors ===")
                        print(resultextract.stderr)

                    yourhash = input(
                        inputs
                        + "Please write the hash that you want to crack (from the results): "
                    )
                    command_lunch_hashcat = (
                        f'hashcat -O -m 1000 "{yourhash}" "{chemin_fichier}"'
                    )
                    command_lunch_hashcats = subprocess.run(
                        command_lunch_hashcat, shell=True, capture_output=True, text=True
                    )
                    print(command_lunch_hashcats.stdout)

                    if command_lunch_hashcats.stderr:
                        print(error + "\n=== Hashcat Errors ===")
                        print(command_lunch_hashcats.stderr)

                elif OS == "Darwin":
                    print(
                        disclamer
                        + "You need to have the system.save and sam.save files in the /home/"
                        + user
                        + "/Desktop/Backup directory to extract hashes from them."
                    )
                    command_for_extracth = (
                        f"impacket-secretsdump "
                        f"-sam /Users/{user}/Desktop/Backup/sam.save "
                        f"-system /Users/{user}/Desktop/Backup/system.save LOCAL"
                    )
                    resultextract = subprocess.run(
                        command_for_extracth, shell=True, capture_output=True, text=True
                    )
                    print(info + "These are the results:\n" + resultextract.stdout)
                    if (
                        resultextract.stderr.startswith("ERROR:")
                        or resultextract.stdout == ""
                    ):
                        print(error + "\n=== Secretsdump Errors ===")
                        print(resultextract.stderr)

                    yourhash = input(
                        inputs
                        + "Please write the hash that you want to crack (from the results): "
                    )
                    command_lunch_hashcat = (
                        f'hashcat -O -m 1000 "{yourhash}" "{chemin_fichier}"'
                    )
                    command_lunch_hashcats = subprocess.run(
                        command_lunch_hashcat, shell=True, capture_output=True, text=True
                    )
                    print(command_lunch_hashcats.stdout)
                    if command_lunch_hashcats.stderr:
                        print(error + "\n=== Hashcat Errors ===")
                        print(command_lunch_hashcats.stderr)
                        print(
                            warning
                            + "You may need to check the system.save and sam.save files in the /Users/"
                            + user
                            + "/Desktop/Backup directory to extract hashes from them."
                        )
                        exit()
                command_lunch_hashcat = (
                    f'"{extraction_path2}" -O -m 1000 "{yourhash}" "{chemin_fichier}"'
                )
                command_lunch_hashcats = subprocess.run(
                    command_lunch_hashcat, shell=True, capture_output=True, text=True
                )
                print(command_lunch_hashcats.stdout)

                if command_lunch_hashcats.stderr:
                    print(error + "\n=== Hashcat Errors ===")
                    print(command_lunch_hashcats.stderr)

            elif request == "n":
                request = (
                    input(inputs + "Do you want to regenerate a new password list (y/n):")
                    .strip()
                    .lower()
                )
                if request == "y":
                    generate_passwords()
                elif request == "n":
                    return
                else:
                    print("Please provide a correct value (y/n)")
            else:
                print(error + "Please provide a correct value (y/n)")