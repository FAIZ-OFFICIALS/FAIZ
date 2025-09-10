import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/DVq6v6lasB5LfIZb4D1NNl?mode=ems_copy_c')
tokyo=platform.architecture()[0]
if tokyo=="32bit":
    os.system('clear')
    print('\033[91;1m [•] 32 Bit Device Not Working')
elif tokyo=="64bit":
    import ctypes
    so_file = "mahar64.cpython-312.so"
    my_module = ctypes.CDLL(so_file)
    # پھر اپنے functions call کریں
