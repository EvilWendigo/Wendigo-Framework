import os
os.system("figlet Wendigo")
os.system("figlet FrameWork")
print("1|bettercap")
print("2|sqlmap")
print("3|spiderfoot")
print("4|wifite")
print("5|recon-ng")

while True:
    console = input("> ")
    if console == "1":
        print("enable monitor mode: Y/N")
        print("has to be typed and in uper case exemple: Y")
        mon = input("> ")
        if mon == "Y":
            os.system("sudo airmon-ng start wlan0")
            os.system("sudo bettercap -iface wlan0mon")
            os.system("sudo airmon-ng stop wlan0mon")
            print("exited monitor mode")
        if mon == "N":
            print("started bettercap without ")
            os.system("sudo bettercap -iface wlan0")
    if console == "2":
        os.system("sqlmap --wizard")
    if console == "3":
        os.system("spiderfoot -l 127.0.0.1:5001")
    if console == "4":
        os.system("sudo wifite")
    if console == "5":
        os.system("recon-ng")
    
