## **Touti Cracker**

"**Touti Cracker(Beta)**" est un outil éducatif développé pour démontrer certains concepts liés à la sécurité informatique, comme la création de listes de mots de passe, la sauvegarde de clés de registre, et les techniques de brute force. **Ce projet est uniquement à des fins éducatives**.

---

**🚨 Avertissement**

**Ce projet n'est pas destiné à un usage malveillant.**\
L'auteur décline toute responsabilité concernant toute activité illégale ou contraire à l'éthique réalisée à l'aide de cet outil. **Utilisez cet outil dans un cadre légal et éthique uniquement.** Vérifiez que vous respectez les lois et réglementations de votre pays avant d'utiliser ce script.

---

**🔧 Fonctionnalités**

1. **Génération de mots de passe** : Créez des listes de mots de passe personnalisées basées sur des informations utilisateur ou aléatoires.
2. **Sauvegarde des registres Windows** : Sauvegarde les clés de registre `SYSTEM` et `SAM` pour analyse locale.
3. **Utilisation de Hashcat** : Automatise l'utilisation de Hashcat pour effectuer des attaques par brute force sur des hachages extraits.
4. **Automatisation** : Simplifie les tâches complexes de sécurité et les rend accessibles aux débutants pour des fins éducatives.

---

**📚 Prérequis**

Avant d'utiliser cet outil, assurez-vous d'avoir les éléments suivants :

- **Python 3.8 ou version supérieure**.
- Les bibliothèques Python listées dans `requirements.txt` (voir section Installation).
- Accès à un système Windows pour exécuter certaines fonctionnalités comme la sauvegarde des registres.

---

**🚀 Installation**

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/Touti-Sudo/Touti-Cracker.git
   ```

2. Accédez au répertoire du projet :

   ```bash
   cd Touti-Cracker
   ```

3. Installez les dépendances Python nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

4. Assurez-vous que l'outil `7-Zip` est installé pour l'extraction automatique de Hashcat et de poser le fichier "Touti Cracker" dans votre bureau.
5. assurez vous de le lancer en mode admin
---

## 🔄 Usage

1. Lancez le script principal avec Python :

   ```bash
   python touti_cracker.py
   ```

2. Suivez les instructions affichées dans le terminal. Par exemple :

   - Entrez les informations pour générer une liste de mots de passe personnalisée.
   - Spécifiez le système d'exploitation cible (Windows 11 est le seul système compatible, mais de nouvelles mises à jour seront disponibles pour le rendre multiplateforme)
   - Lancez Hashcat pour effectuer une attaque par brute force sur un hachage spécifique.

3. Les résultats (par exemple, les mots de passe générés) seront sauvegardés sur le bureau de l'utilisateur dans un fichier texte.

---

## 📚 Exemple de Scénario

Voici un scénario simple pour utiliser cet outil :

1. Vous voulez tester la sécurité d'un mot de passe Windows.
2. Lancez le script et sauvegardez les clés de registre SYSTEM et SAM.
3. Extrayez les hachages des mots de passe avec `secretsdump.py`.
4. Utilisez Hashcat pour effectuer une attaque par brute force avec une liste de mots de passe personnalisée.

---

## 🔒 Licence

Ce projet est sous [licence MIT](./LICENSE). Consultez le fichier LICENSE pour plus de détails.

**Clause supplémentaire** : Ce projet est fourni à des fins éducatives uniquement. L'auteur n'assume aucune responsabilité pour toute utilisation illégale ou abusive.

---

## 👨‍💻 Auteur

- **Touti (Anes)**\
  Pour toute question ou retour, contactez-moi via mon [GitHub](https://github.com/\[VotreNomOuPseudonyme]).

---

## 🔗 Liens Utiles

- [Site officiel de Hashcat](https://hashcat.net/hashcat/)
- [Documentation de Python](https://docs.python.org/3/)

