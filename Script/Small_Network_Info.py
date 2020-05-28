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
    chs = int(input("Enter your choice: "))
    return chs


chs = welcome


def StatusMonitor(mon):
    if(mon == 1):
        hostname = input("\n Input hostname: \n")
        return os.system("ping " + hostname)
    elif(mon == 2):
        DNSShow = os.system("ipconfig /displaydns")
        print(DNSShow)
        return os.system("ipconfig /flushdns")
    elif(mon == 3):
        print("Trace IP route")
        IPtoTrace = input("Input IP: \n")
        return os.system("tracert " + IPtoTrace)
    elif(mon == 4):
        print("IP information info")
        return os.system("ipconfig /all")
    elif(mon == 5):
        print("System Info")
        return os.system("systeminfo")
    elif(mon == 0):
        print("Bye Bye ")
        return exit(0)
while chs is not 0:
    StatusMonitor(welcome())
