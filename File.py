elif FAIZ == "64bit":
    try:
        # پہلے .so فائل چلانے کی کوشش کریں
        from filemaking import *
    except:
        # اگر نہ چلے تو .py فائل چلائیں
        exec(open("filemaking.py").read())
