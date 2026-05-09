import os,platform
os.system('git pull --quiet 2>/dev/null')
djs=platform.architecture()[0]
if djs=="32bit":
    os.system('clear')
    print('\033[91;1m [+] 32 Bit Device Not Working')
elif djs=="64bit":
    __import__("d2")
