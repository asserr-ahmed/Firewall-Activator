import platform
import subprocess
import argparse

def run(cmd):
    """Run a system command and return output."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

# WINDOWS #

def win_status():
    return run("netsh advfirewall show allprofiles")

def win_enable():
    return run("netsh advfirewall set allprofiles state on")

def win_disable():
    return run("netsh advfirewall set allprofiles state off")

#  MACOS #

def mac_status():
    return run("/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate")

def mac_enable():
    return run("sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on")

def mac_disable():
    return run("sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate off")

# MAIN LOGIC #

def main():
    parser = argparse.ArgumentParser(description="Cross‑platform Firewall Manager")
    parser.add_argument("--status", action="store_true", help="Check firewall status")
    parser.add_argument("--enable", action="store_true", help="Enable firewall")
    parser.add_argument("--disable", action="store_true", help="Disable firewall")

    args = parser.parse_args()
    system = platform.system()

    if system == "Windows":
        if args.status:
            out, err = win_status()
        elif args.enable:
            out, err = win_enable()
        elif args.disable:
            out, err = win_disable()
        else:
            print("No action provided.")
            return

    elif system == "Darwin":  # macOS
        if args.status:
            out, err = mac_status()
        elif args.enable:
            out, err = mac_enable()
        elif args.disable:
            out, err = mac_disable()
        else:
            print("No action provided.")
            return

    else:
        print("Unsupported OS.")
        return

    print(out)
    if err:
        print("Errors:", err)

if __name__ == "__main__":
    main()