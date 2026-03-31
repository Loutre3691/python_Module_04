if __name__ == "__main__":
    print("\033[1;35m\n==== CYBER ARCHIVES - VAULT SECURITY SYSTEM"
          " ===\033[0m\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    with open("vault.txt", "w") as f:
        f.write("SECURE EXTRACTION:\n")
        f.write("[CLASSIFIED] Quantum encryption keys recovered\n")
        f.write("[CLASSIFIED] Archive integrity: 100%\n")
        f.write("\nSECURE PRESERVATION:\n")
        f.write("[CLASSIFIED] New security protocols archived\n")
        f.write("Vault automatically sealed upon completion\n")
    with open("vault.txt", "r") as f:
        print(f.read())

    print("All vault operations completed with maximum security.")
