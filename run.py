import os
import platform
import importlib.util

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
        # پہلے .so فائل کو لوڈ کرنے کی کوشش کریں
        so_file = "filemaking.cpython-312.so"
        if os.path.exists(so_file):
            # صحیح طریقے سے ماڈیول لوڈ کریں
            spec = importlib.util.spec_from_file_location("filemaking_module", so_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # ماڈیول کے main فنکشن کو کال کریں
            if hasattr(module, 'Menu'):
                module.Menu()
            else:
                print("Error: Menu function not found in .so file")
                # fallback to .py file
                import filemaking
        else:
            print(".so file not found, using .py file")
            import filemaking
            
    except Exception as e:
        print(f'\033[91;1m [•] Error loading .so file: {e}')
        print('\033[93;1m [•] Falling back to Python file...')
        try:
            import filemaking
        except Exception as py_error:
            print(f'\033[91;1m [•] Python file error: {py_error}')
