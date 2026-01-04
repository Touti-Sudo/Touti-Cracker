


import os
import subprocess


def save_registers(OS,user,info,error,the_link,inputs):
            if OS == "Windows":
                chemin_backup = "C:\\Users\\" + user + "\\Desktop\\Backup"
            elif OS == "Linux":
                chemin_backup = "/home/" + user + "/Desktop/Backup"
            elif OS == "Darwin":
                chemin_backup = "/Users/" + user + "/Desktop/Backup"
            registres = input(
                inputs
                + 'You want to save YOUR regestry keys ? (y/n) "if you have the target regestry keys then put them in '
                + chemin_backup
                + '"'
                + " :"
            )

            if registres.lower() == "y":
                if OS == "Windows":
                    print(info + "Saving Registry keys...")
                    chemin_system_save = os.path.join(chemin_backup, "system.save")
                    chemin_sam_save = os.path.join(chemin_backup, "sam.save")

                    os.makedirs(chemin_backup, exist_ok=True)

                    if os.path.exists(chemin_system_save) and os.path.exists(
                        chemin_sam_save
                    ):
                        print(
                            info
                            + "Registry keys already saved. Skipping registry saving..."
                        )
                        return

                    commande_system = f'reg save HKLM\\system "{chemin_system_save}"'
                    commande_sam = f'reg save HKLM\\sam "{chemin_sam_save}"'

                    result_system = subprocess.run(
                        commande_system, shell=True, capture_output=True, text=True
                    )
                    if result_system.returncode == 0:
                        print(info + "System registry key saved successfully.")
                    else:
                        print(
                            error
                            + f"{result_system.stderr}\nError saving system registry key , high privilege may be required so please restart Touti Cracker at admin mod"
                        )
                        exit()

                    result_sam = subprocess.run(
                        commande_sam, shell=True, capture_output=True, text=True
                    )
                    if result_sam.returncode == 0:
                        print(info + "SAM registry key saved successfully.")
                    else:
                        print(
                            error
                            + f"{result_sam.stderr}\nError saving SAM registry key , high privilege may be required so please restart Touti Cracker at admin mod"
                        )
                        exit()
                else:

                    print(
                        error
                        + "The feature of saving registers is not available for Linux and Mac yet but it will be in the next update and you can still put target registers in (/Desktop/Backup) check my github account for more details: "
                        + the_link
                    )
            elif registres.lower() == "n":
                pass
            else:
                print(error + "Please provide a correct value (y/n)")