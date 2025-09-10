import os
import platform
import subprocess
import time
import webbrowser

# Clear the screen
os.system('clear')

# Git pull quietly
try:
    subprocess.run(['git', 'pull'], capture_output=True)
except:
    pass  # Silently continue if git pull fails

print('\033[97;1m [•] Join Whatsapp Group')

# Open WhatsApp group in background without blocking
try:
    # For Linux
    if platform.system() == 'Linux':
        subprocess.Popen(['xdg-open', 'https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl?mode=ems_copy_c'], 
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # For Windows
    elif platform.system() == 'Windows':
        webbrowser.open('https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl?mode=ems_copy_c', new=0, autoraise=True)
    # For macOS
    else:
        subprocess.Popen(['open', 'https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl?mode=ems_copy_c'], 
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    print('\033[91;1m [•] Error opening WhatsApp group')

# Add a small delay to ensure the browser opens before continuing
time.sleep(2)

# Check architecture and import appropriate module
tokyo = platform.architecture()[0]
if tokyo == "32bit":
    os.system('clear')
    print('\033[91;1m [•] 32 Bit Device Not Working')
elif tokyo == "64bit":
    try:
        # Try to import the compiled module
        __import__("charsi64")
    except ImportError:
        print('\033[91;1m [•] Error: Could not import charsi64 module')
        print('\033[91;1m [•] Make sure charsi64.cpython-312.so is in the correct directory')
