import os
import secrets


def generate_passwords(info, first, second, inputs, OS, user, error):
    print(info + first + " Customyze")
    print(info + second + " Randomyze")
    choice = input(inputs + "Please choose an option: ")
    if choice == "1":
        print(info + "customizing password generator...")
        if OS == "Windows":
            chemin_fichier = (
                "C:\\Users\\" + user + "\\Desktop\\Touti_Cracker\\passwordlist.txt"
            )
        if OS == "Linux":
            chemin_fichier = "/home/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
        if OS == "Darwin":
            chemin_fichier = (
                "/Users/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
            )
        number_of_generated_words = int(
            input(
                inputs
                + "How many passwords do you want to generate for brute force? : "
            )
        )
        informations = []

        print(
            inputs + "Provide information to generate passwords (Press Enter to skip ):"
        )
        Name = input(inputs + "First Name: ") or ""
        Family = input(inputs + "Family Name: ") or ""
        Nick = input(inputs + "Nick Name: ") or ""
        birth = input(inputs + "Date of birth (DD/MM/YYYY): ") or ""
        pet = input(inputs + "Pet Name: ") or ""
        country = input(inputs + "Country: ") or ""
        city = input(inputs + "City: ") or ""

        informations.extend([Name, Family, Nick, birth, pet, country, city])
        informations = [info for info in informations if info]

        os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)

        with open(chemin_fichier, "w", encoding="utf-8") as fichier:
            print(info + "Generated Passwords:")
            for i in range(number_of_generated_words):
                longeur = secrets.choice(range(3, 16))
                mot_de_passe = "".join(
                    secrets.choice(informations) for _ in range(longeur)
                )
                mot_de_passee = f"{i + 1}.{mot_de_passe}"
                mot_de_passee = mot_de_passee.split(".", 1)[-1].strip()
                print(mot_de_passee)
                fichier.write(mot_de_passee + "\n")
    elif choice == "2":
        if OS == "Windows":
            chemin_fichier = (
                "C:\\Users\\" + user + "\\Desktop\\Touti_Cracker\\passwordlist.txt"
            )
        elif OS == "Linux":
            chemin_fichier = "/home/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
        elif OS == "Darwin":
            chemin_fichier = (
                "/Users/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
            )
        chifrre = "0123456789"
        lettre = "azertyuiopmlkjhgfdsqwxcvbn"
        lettreup = lettre.upper()
        caractere_special = "}@()é&à=+-*/ç_²$ù^!;,"
        number_of_generated_words = int(
            input(
                inputs
                + "How many passwords do you want to generate for brute force? : "
            )
        )
        liste_complete = list(lettre + chifrre + lettreup + caractere_special)
        dossier = os.path.dirname(chemin_fichier)
        if not os.path.exists(dossier):
            os.makedirs(dossier)

        with open(chemin_fichier, "w", encoding="utf-8") as fichier:
            print(info + "Generated Passwords:")
            for i in range(number_of_generated_words):
                longeur = secrets.choice(range(3, 17))
                mot_de_passe = "".join(
                    secrets.choice(
                        liste_complete,
                    )
                    for _ in range(longeur)
                )
                mot_de_passee = mot_de_passee.split(".", 1)[-1].strip()
                print(mot_de_passee)
                fichier.write(mot_de_passee + "\n")
    else:
        print(error + "Please enter a valid choice (1/2).")
        return
    print(info + f"All passwords have been saved to: {chemin_fichier}")
