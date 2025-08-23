import os
import platform

# Termux کے home directory میں جائیں
os.chdir(os.path.expanduser("~/FAIZ"))

os.system('git pull --quiet 2>/dev/null')
os.system("clear")

print('\033[97;1m [•] Please join our WhatsApp group:')
print('\033[94;1m https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl')
print('\033[97;1m [•] Press Enter to continue...')
input()

FAIZ = platform.architecture()[0]
if FAIZ == "32bit":
    os.system('clear')
    print('\033[91;1m [•] 32 Bit Device Not Working')
elif FAIZ == "64bit":
    import filemaking
