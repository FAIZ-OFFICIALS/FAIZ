import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\x1b[38;5;216m [\x1b[38;5;161m•\x1b[38;5;216m] \x1b[38;5;188mJoin Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl')
faiz=platform.architecture()[0]
if faiz=="32bit":
    os.system('clear')
    print('\033[91;1m [•] 32 Bit Device Not Working')
elif tokyo=="64bit":
    __import__("tokyo64")
