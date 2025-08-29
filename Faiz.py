import os, platform

# Change to the script's directory for proper file access
os.chdir(os.path.dirname(os.path.abspath(__file__)))

os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl?mode=ac_t')

FAIZ = platform.architecture()[0]
if FAIZ == "32bit":
    os.system('clear')
    print('\033[91;1m [•] 32 Bit Device Not Working')
elif FAIZ == "64bit":
    try:
        __import__("mahar")
    except Exception as e:
        print(f"Error loading module: {e}")
