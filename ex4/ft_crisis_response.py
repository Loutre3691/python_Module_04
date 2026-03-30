
if __name__ == "__main__":
    print("\033[1;35m\n==== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM "
          "===\033[0m\n")

    print("\033[1;33mCRISIS ALERT: Attempting access to 'lost_archive.txt' "
          ".\033[0m")
    try:
        with open("lost_archive.txt", "r") as f:
            print(f.read())
            print("STATUS: Crisis handled, system stable\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, security maintained\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    print("\033[1;33mCRISIS ALERT: Attempting access to 'classified_vault.txt'"
          "...\033[0m")
    try:
        with open("classified_vault.txt", "r") as f:
            print(f.read())
            print("STATUS: Crisis handled, system stable\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, security maintained\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    print("\033[1;33mROUTINE ACCESS: Attempting access to "
          "'standard_archive.txt'...\033[0m")
    try:
        with open("standard_archive.txt", "r") as f:
            print(f"SUCCESS: Archive recovered - {f.read()}")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, security maintained\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    print("\033[1;35mAll crisis scenarios handled successfully. Archives "
          "secure.\033[0m")
