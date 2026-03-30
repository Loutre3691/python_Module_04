def crisis_handler(fichier: str) -> None:
    print(f"\033[1;33mCRISIS ALERT: Attempting access to {fichier}"
          ".\033[0m")
    try:
        with open(fichier, "r") as f:
            print(f.read())
            print("STATUS: Crisis handled, system stable\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, security maintained\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")


def routine_access(fichier: str) -> None:
    print(f"\033[1;33mROUTINE ACCESS: Attempting access to "
          f"{fichier}...\033[0m")

    try:
        with open(fichier, "r") as f:
            print(f"SUCCESS: Archive recovered - {f.read()}")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, security maintained\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")


if __name__ == "__main__":
    print("\033[1;35m\n==== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM "
          "===\033[0m\n")

    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    routine_access("standard_archive.txt")

    print("\033[1;35mAll crisis scenarios handled successfully. Archives "
          "secure.\033[0m")
