import time
from time import sleep
import os
time.sleep(0.3)
os.system('cls' if os.name == 'nt' else 'clear')
import random
import string
import ctypes
from colorama import Fore, Back, Style
try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.9'} pip install discord_webhook'\nPress enter to exit") # Tell the user it has not been installed and how to install it
    exit()
try:
    import requests
except ImportError:
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.9'} pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
    exit()
class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes - Developed by cutieQue.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            os.system('cls' if os.name == 'nt' else 'clear')
            ctypes.windll.kernel32.SetConsoleTitleW("Discord Nitro Generator and Checker! | NOT STARTED GENERATOR / CHECKER | Developed by: cutieQue")
        else:
            print(f'\33]0;Discord Nitro Generator and Checker! | NOT STARTED GENERATOR / | CHECKER Developed by: cutieQue\a', end='', flush=True)

        print(f"""{Fore.RED + Style.BRIGHT}
██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ███╗░░██╗██╗████████╗██████╗░░█████╗░
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░{Fore.RESET}""")
        self.slowType(f"{Fore.LIGHTYELLOW_EX}Generator and Checker!{Fore.RESET}", .01)
        time.sleep(0.5)
        self.slowType(f"{Fore.LIGHTBLUE_EX}Developed by: cutieQue{Fore.RESET}\n", .01)
        time.sleep(0.4)
        self.slowType(f"{Fore.LIGHTRED_EX}\nHow Many Codes? \n[>] {Fore.RESET}", .01, newLine = False)


        num = int(input(''))
        self.slowType(f"{Fore.LIGHTYELLOW_EX}Enter a Discord Webhook link or press Enter to Ignore. \n[>] {Fore.RESET}", .01, newLine = False)
        url = input('')
        webhook = url if url != "" else None
        sleep(0.5)
        print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}------------------------------------------------------------------------------------------------------------------------\n")


        valid = []
        invalid = 0

        for i in range(num):
            try:
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f" Error: {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Nitro Generator & Checker! | {len(valid)} Valid Nitro Codes Found | {invalid} Invalid Nitro Codes Found | RUNNING GENERATOR / CHECKER | Developed by cutieQue")
                print("")
            else:
                print(f'\33]0;Discord Nitro Generator & Checker! - {len(valid)} Valid Nitro Codes Found | {invalid} Invalid Nitro Codes Found | RUNNING GENERATOR / CHECKER - Developed by cutieQue\a', end='', flush=True)

        print(f"""
{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}------------------------------------------------------------------------------------------------------------------------
{Fore.LIGHTYELLOW_EX}Results:
{Fore.LIGHTGREEN_EX}Valid:{Fore.RESET} {len(valid)}
{Fore.RESET}{Fore.LIGHTRED_EX}Invalid:{Fore.RESET} {invalid}
{Fore.LIGHTGREEN_EX}Valid Nitro Codes:{Fore.RESET} {', '.join(valid )}{Fore.RESET}""")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Nitro Generator & Checker! | {len(valid)} Valid Nitro Codes Found | {invalid} Invalid Nitro Codes Found | STOPPED GENERATOR / CHECKER | Developed by cutieQue")

        input(f"{Fore.WHITE}\nPress Enter to Exit!")


    def slowType(self, text, speed, newLine = True):
        for i in text:
            print(i, end = "", flush = True)
            time.sleep(speed)
        if newLine:
            print()

    def generator(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print("Wait, Generating for you")

            start = time.time()

            for i in range(amount):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))

                file.write(f"https://discord.gift/{code}\n")

            print(f"Generated {amount} codes! | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url)

                if response.status_code == 200:
                    print(f" Valid:{Fore.RESET} {nitro} ")
                    valid.append(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"**Valid Nito Code detected!** @everyone \n{nitro}"
                        ).execute()
                    else:
                        break

                else:
                    print(f" Invalid:{Fore.RESET} {nitro} ")
                    invalid += 1

        return {f"{Fore.LIGHTGREEN_EX}valid" : valid, f"{Fore.RED}invalid" : invalid}

    def quickChecker(self, nitro, notify = None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX} Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes - Developed by cutieQue.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"**Valid Nito Code detected!** @everyone \n{nitro}"
                ).execute()

            return True

        else:
            print(f"{Fore.RED} Invalid:{Fore.RESET} {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            return False

if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
