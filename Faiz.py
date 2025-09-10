import os, platform

os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl?mode=ems_copy_c')

FAIZ = platform.architecture()[0]
if FAIZ == "32bit":
    os.system('clear')
    print('\033[91;1m [•] 32 Bit Device Not Working')
elif FAIZ == "64bit":
    # براہ راست Python فائل چلائیں
    os.system('python mahar64.py')
