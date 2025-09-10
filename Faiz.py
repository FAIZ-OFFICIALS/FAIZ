import os
import platform
import subprocess
import sys

# Pull updates and clear screen
os.system('git pull --quiet 2>/dev/null')
os.system("clear")

print('\033[97;1m [+] JOIN WHATSAPP GROUP')

# Open WhatsApp without blocking
subprocess.Popen(['xdg-open', 'https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl?mode=ems_copy_c'], 
                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Check architecture
Faiz = platform.architecture()[0]

if Faiz == "32bit":
    os.system('clear')
    print('\033[91;1m [+] 32 Bit Device Not Working')
    sys.exit(1)

# For 64bit devices
try:
    # First check if file exists
    if not os.path.exists("charsi64.cpython-312.so"):
        print('\033[91;1m [+] Error: Compiled module not found!')
        print('\033[91;1m [+] Please make sure charsi64.cpython-312.so is in the same directory')
        sys.exit(1)
    
    # Make sure the file has execute permissions
    os.system('chmod +x charsi64.cpython-312.so 2>/dev/null')
    
    # Try to import the module
    from charsi64 import main
    print('\033[92;1m [+] Module imported successfully!')
    
    # Run the main function from the module
    main()
    
except ImportError as e:
    print(f'\033[91;1m [+] Import Error: {e}')
    print('\033[91;1m [+] This usually means:')
    print('\033[91;1m [+] 1. Python version is not 3.12')
    print('\033[91;1m [+] 2. The module is not compatible with your system')
    
    # Check Python version
    py_version = sys.version_info
    print(f'\033[93;1m [+] Your Python version: {py_version.major}.{py_version.minor}.{py_version.micro}')
    print('\033[93;1m [+] Required Python version: 3.12.x')
    
except Exception as e:
    print(f'\033[91;1m [+] Unexpected error: {e}')
