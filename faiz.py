import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\x1b[38;5;216m [\x1b[38;5;161m•\x1b[38;5;216m] \x1b[38;5;188mJoin Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl')
faiz=platform.architecture()[0]
if faiz=="32bit":
    os.system("clear")
    exit('\x1b[38;5;216m [\x1b[38;5;161m•\x1b[38;5;216m] \033[91;1mSorry Bro 32 Bit Devices Not Supported')
elif faiz=="64bit":
    __import__("faiz64")
