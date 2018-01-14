"""Python network check"""
import os

line = "--------------------------"
print(line)
print(" Network and System Info \n Version 1.0 ")
print(line)


def welcome():
    print(line)
    print(" 1.Ping \n 2.Flush DNS \n 3.Trace IP \n 4.Show IP info \n 5.System Info \n 0.Exit \n")
    print(line)
    odabir = int(input("Enter your choice: "))
    return odabir


odabir = welcome


def StatusMonitor(pomocna):
    if(pomocna == 1):
        hostname = input("\n Unesite hostname: \n")
        return os.system("ping " + hostname)
    elif(pomocna == 2):
        DNSShow = os.system("ipconfig /displaydns")
        print(DNSShow)
        return os.system("ipconfig /flushdns")
    elif(pomocna == 3):
        print("Trace IP route")
        IPtoTrace = input("Unesite IP: \n")
        return os.system("tracert " + IPtoTrace)
    elif(pomocna == 4):
        print("IP information info")
        return os.system("ipconfig /all")
    elif(pomocna == 5):
        print("System Info")
        return os.system("systeminfo")
    elif(pomocna == 0):
        print("Bye Bye ")
        return exit(0)
while odabir is not 0:
    StatusMonitor(welcome())
