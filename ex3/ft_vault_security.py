if __name__ == "__main__":
    print("\033[1;35m\n==== CYBER ARCHIVES - VAULT SECURITY SYSTEM"
          "===\033[0m\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    with open("fichier.txt", "w") as f:
        f.write("SECURE EXTRACTION:\n")
        f.write("[CLASSIFIED] Quantum encryption keys recovered\n")
        f.write("[CLASSIFIED] Archive integrity: 100%\n")
        f.write("\nSECURE PRESERVATION:\n")
        f.write("[CLASSIFIED] New security protocols archived\n")
        f.write("Vault automatically sealed upon completion\n")
    with open("fichier.txt", "r") as f:
        print(f.read())



# utilisation "with" pour une gestion correcte des fichier
# with ferme automatiquement les fichiers meme si erreur
#
# protcole sac red (secu):
# - ouverture du coffre
# - s'executent en secu a l'in de la barriere de protection
# - le coffre se referme de lui-meme en cas de probleme
#
# protocoles de secu du coffre:
# - implementations des operations des fichiers securises en utilisant "with"
# pour la lecture des donnees classee et preserver les news informations
# le prog doit demontrer le scellement auto du vault que ca reussisse ou 
# pas
# journalisation de secu pro tout au long du processus