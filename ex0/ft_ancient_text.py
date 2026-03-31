if __name__ == "__main__":
    print("\033[1;35m\n==== CYBER ARCHIVES - DATA RECOVERY SYSTEM "
          "===\033[0m\n")
    try:
        file = open("ancient_fragment.txt")
        print(f"Accessing storage Vault: {file.name}")
        print("connection established...\n")
        print(file.read())

    except FileNotFoundError:
        print("\033[0;31mError: Storage vault not found\033\n[0m")
        exit()

    print(file.read())
    print("Data recovery complete. Storage unit disconnected.")
    file.close()
