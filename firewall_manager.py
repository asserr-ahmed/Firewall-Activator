import os
import platform

def enable_firewall():
    system = platform.system()

    if system == "Darwin":  # macOS
        os.system('sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on')
        print("Firewall enabled on macOS.")

    elif system == "Windows":
        os.system('netsh advfirewall set allprofiles state on')
        print("Firewall enabled on Windows.")

    else:
        print("Unsupported operating system.")

def disable_firewall():
    system = platform.system()

    if system == "Darwin":  # macOS
        os.system('sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate off')
        print("Firewall disabled on macOS.")

    elif system == "Windows":
        os.system('netsh advfirewall set allprofiles state off')
        print("Firewall disabled on Windows.")

    else:
        print("Unsupported operating system.")

def check_firewall_status():
    system = platform.system()

    if system == "Darwin":  # macOS
        os.system('/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate')

    elif system == "Windows":
        os.system('netsh advfirewall show allprofiles')

    else:
        print("Unsupported operating system.")

def main():
    while True:
        print("\n=== Firewall Manager ===")
        print("1. Enable Firewall")
        print("2. Disable Firewall")
        print("3. Check Firewall Status")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            enable_firewall()
        elif choice == "2":
            disable_firewall()
        elif choice == "3":
            check_firewall_status()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1–4.")

if __name__ == "__main__":
    main()
