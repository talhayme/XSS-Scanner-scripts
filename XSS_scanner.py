import requests
import time
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
print(Fore.GREEN + "XSS DETECTOR" + Fore.RED + "By CS" + Style.RESET_ALL)
time.sleep(2)
print()
pog = input("POST or GET ? (p/g) : ")
if pog == "g":
    try:
            site = input("Site to test ? (with parameters) : ") # target
            r = requests.post(site, headers=header)
            time.sleep(1)
            print()
            print(Fore.GREEN + "the site respond !" + Style.RESET_ALL)
    except:
            print()
            print("does the script respond...")
            time.sleep(3)
            print()
            print(Fore.RED + "The site doesn't respond, try again. (with https:// or http:// ...)" + Style.RESET_ALL)
            sys.exit(0)
    print()
    try:
                repertoirepayload = input(" wordlist.txt/rtf directory : ") # here goes the link with xss wordlist
                reper = open(repertoirepayload, "r")
    except FileNotFoundError:
            print()
            print("The File " + Fore.RED + repertoirepayload + Style.RESET_ALL + " doesn't exist, try again !")
            sys.exit(0)
    print()
    print(Fore.GREEN + "Test in process... \n")
    time.sleep(2)
    f= open(repertoirepayload, "r")
    l = 1
    for line in f:
        print()
        print(Fore.GREEN + "I test the payload " + str(1))
        if line in requests.get(site + line, headers=header).text:
            print(Fore.RED + "XSS FOUND HERE : \n" + Style.RESET_ALL)
            print(requests.get(site + line, headers=header).url)
        else:
            print(Fore.RED + "The payload" + str(l) + " does not trigger the XSS Filter." + Style.RESET_ALL)
            print()
            l += 1

elif pog == "p":
    try:
        site = input("URL to test: ")
        data = input("POST DATA : ")
        r = requests.post(site, headers=header, data=data)
        time.sleep(1)
        print()
        print(Fore.GREEN + "The site respond" + Style.RESET_ALL)
    except:
        print()
        print("Does the site respond...")
        time.sleep(3)
        print()
        print(Fore.RED + "The site doesn't respond, try again (with https:// or http:// etc..)" + Style.RESET_ALL)
        sys.exit(0)
    print()
    try:
        repertoirepayload = input("wordlist.txt directory: ")
        reper = open(repertoirepayload, "r")
    except FileNotFoundError:
        print()
        print("The file " + Fore.RED + repertoirepayload + Style.RESET_ALL + " doesn't exist, try again")
        sys.exit(0)
    print()
    print(Fore.GREEN + "Test in process...\n")
    time.sleep(2)
    f = open(repertoirepayload, "r")
    l = 1
    for line in f:
        print(Fore.GREEN + "I test the payload " + str(l) + "...\n")
        if line in requests.get(site + line, headers=header, data=data).text:
            print(Fore.RED + "XSS FOUND HERE:\n" + Style.RESET_ALL)
            print(requests.get(site + line, headers=header, data=data.url + " Post DATA = " + data + "\n"))
        else:
            print(Fore.RED + "The payload" + str(l) + " does not trigger the XSS Filter." + Style.RESET_ALL)
            print()
            l += 1
else:
    print("Unknown answer.")
    sys.exit(0)
