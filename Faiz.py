import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [+] JOIN WHATSAPP GROUP')
os.system('xdg-open https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl?mode=ems_copy_c')
djs=platform.architecture()[0]
if charsi64=="32bit":
    os.system('clear')
    print('\033[91;1m [+] 32 Bit Device Not Working')
elif charsi64=="64bit":
    __import__("charsi64")
