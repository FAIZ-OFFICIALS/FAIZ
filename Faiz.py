import os, platform

os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/BmxmNHAMjLj5i59vqB2uKw')

tokyo = platform.architecture()[0]
if tokyo == "32bit":
    os.system('clear')
    print('\033[91;1m [•] 32 Bit Device Not Working')
elif tokyo == "64bit":
    try:
        # پہلے compiled module import کرنے کی کوشش کریں
        __import__("mahar64")
    except ImportError:
        # اگر compiled module نہ ملے تو source file سے compile کریں
        print('\033[93;1m [•] Compiling mahar64 module...')
        try:
            # Cython install کریں اگر نہ ہو تو
            os.system('pip install cython --quiet > /dev/null 2>&1')
            # Compile کریں
            os.system('cythonize -i -2 mahar64.py > /dev/null 2>&1')
            # دوبارہ import کرنے کی کوشش کریں
            __import__("mahar64")
            print('\033[92;1m [•] Compilation successful!')
        except Exception as e:
            print(f'\033[91;1m [•] Compilation failed: {e}')
            exit()
