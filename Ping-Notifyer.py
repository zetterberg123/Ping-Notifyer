import os
import sys
try:
    from win10toast import ToastNotifier # pip install win10toast
except ImportError:
    print("Error! You need to install win10toast with \"pip install win10toast\"")
    exit()

# Text colors
os.system("")
class colors:
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def main():
    # Ask user for ip to ping
    try:
        hostname = sys.argv[1]
        print(colors.CYAN + "IP" + colors.ENDC + ": " + hostname)
    except:
        hostname = input(colors.CYAN + "IP to ping" + colors.ENDC + ": ")

    print(colors.GREEN + "Pinging... You can now minimize this window!")
    print(f"============================================" + colors.ENDC)

    while True:
        # Do ping
        response = os.system("ping " + hostname)

        # Check the response...
        if response == 0:
            print(colors.GREEN + hostname, "is up!" + colors.ENDC)

            # Show notification
            toast = ToastNotifier()
            toast.show_toast("Ping",(hostname + " is online!"), duration=10, threaded=True)

            # and quit
            raise SystemExit
        else:
            print(colors.FAIL + hostname, "is down! Trying again..." + colors.ENDC)

# start
if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        print(colors.FAIL + "Exiting..." + colors.ENDC)
        exit()
    except KeyboardInterrupt:
        print(colors.FAIL + " Interrupted")
        input(colors.WARNING + "Press enter to exit..." + colors.ENDC)
        exit()