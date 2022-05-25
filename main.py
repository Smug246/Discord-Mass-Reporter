# Made with ♥️ by Smug

import requests
import colorama
import os
import threading
from threading import Thread
from colorama import Fore, Style

s = Style.BRIGHT

os.system(f'cls & mode 83,24 & title Discord Mass Reporter - Made By Smug')

print(f"""{s+Fore.MAGENTA}   ____    _                                   _     __  __                       
  |  _ \  (_)  ___    ___    ___    _ __    __| |   |  \/  |   __ _   ___   ___   
  | | | | | | / __|  / __|  / _ \  | '__|  / _` |   | |\/| |  / _` | / __| / __|   
  | |_| | | | \__ \ | (__  | (_) | | |    | (_| |   | |  | | | (_| | \__ \ \__ \  
  |____/  |_| |___/  \___|  \___/  |_|     \__,_|   |_|  |_|  \__,_| |___/ |___/ {Fore.RESET} {s+Fore.WHITE}
              ____                                  _                 
             |  _ \    ___   _ __     ___    _ __  | |_    ___   _ __ 
             | |_) |  / _ \ | '_ \   / _ \  | '__| | __|  / _ \ | '__|
             |  _ <  |  __/ | |_) | | (_) | | |    | |_  |  __/ | |   
             |_| \_\  \___| | .__/   \___/  |_|     \__|  \___| |_|   
                            |_| {Fore.RESET}

{s+Fore.MAGENTA} 0 > {Fore.RESET}Reasons:
{s+Fore.MAGENTA} 1 > {Fore.RESET}Illegal Content
{s+Fore.MAGENTA} 2 > {Fore.RESET}Harrassment
{s+Fore.MAGENTA} 3 > {Fore.RESET}Spam Or Phishing Links
{s+Fore.MAGENTA} 4 > {Fore.RESET}Self Harm
{s+Fore.MAGENTA} 5 > {Fore.RESET}NSFW Content
""")

token = input(f"{s+Fore.MAGENTA} > Token{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)

if r.status_code == 200:
        pass
else:
        print(f"{s+Fore.RED} > Invalid Token")
        print(f"{s+Fore.RED} > Press Anything To Exit. . .")
        input()

reason1 = input(f"{s+Fore.MAGENTA} > Choose A Reason{Fore.RESET}: ")
guild_id1 = input(f"{s+Fore.MAGENTA} > Server ID{Fore.RESET}: ")
channel_id1 = input(f"{s+Fore.MAGENTA} > Channel ID{Fore.RESET}: ")
message_id1 = input(f"{s+Fore.MAGENTA} > Message ID{Fore.RESET}: ")

def MassReport():
  global sent
  headers = {
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"{s+Fore.MAGENTA} > {Fore.RESET}Sent Report ID {message_id1}")
      os.system(f'Sending Reports. . .')
      sent += 1
      
    elif r.status_code == 401:
      print(f"{Fore.RED} > Invalid token")
      input()
      exit()
    else:
      print(f"{Fore.RED} > Error")


print()
for i in range(500, 1000):
    Thread(target=MassReport).start()
