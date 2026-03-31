if __name__ == "__main__":
    print("\033[1;35m\n===  CYBER ARCHIVES - PRESERVATION SYSTEM "
          "===\033[0m\n")
    file_w = open("new_discovery.txt", "w")
    print(f"Initializing new storage unit: {file_w.name}")
    print("Storage unit created successfully...\n")

    file_w.write("Inscribing preservation data...\n")
    file_w.write("[ENTRY 001] New quantum algorithm discovered\n")
    file_w.write("[ENTRY 002] Efficiency increased by 347%\n")
    file_w.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    file_w.close()

    try:
        file_read = open("new_discovery.txt", "r")
        print(file_read.read())
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive {file_read.name} ready for long-term preservation.")

    except FileNotFoundError:
        print("\033[0;31mError: Storage vault not found\033\n[0m")
        exit()

    file_read.close()
