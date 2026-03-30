import sys

if __name__ == "__main__":
    print("\033[1;35m\n==== CYBER ARCHIVES - COMMUNICATION SYSTEM "
          "===\033[0m\n")
    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from {id}: {status}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels \
verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")
