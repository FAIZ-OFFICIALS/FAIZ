import os
import platform
import importlib.util

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
    try:
        so_file = "filemaking.cpython-312.so"
        if os.path.exists(so_file):
            spec = importlib.util.spec_from_file_location("filemaking_module", so_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, 'Menu'):
                module.Menu()
            else:
                import filemaking
        else:
            import filemaking
            
    except Exception as e:
        print(f'\033[91;1m [•] Error: {e}')
        import filemaking
