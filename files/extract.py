import requests as nabil
import bs4
import os 
import time 
logo = """ \033[1;94m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/

Created By : \033[1;96mNabil-Rahman |\033[1;0m [V 1.1.1]

\033[1;32m------------------------------------------
\33[93m AUTHOR  : Team DarkWeb T-D
\33[93m GITHUB  : github.com/Nabil-Official
\33[93m FB      : nabil.404
\033[1;32m------------------------------------------
"""

def main():
    os.system('clear')
    print logo 
    print 
    url = raw_input('\033[1;31m>> \033[1;32mEnter Site Url (http://site.com) :\033[1;35m ')
    m = nabil.get(url)
    if m.status_code != 200:
       print ('\033[1;31m[+] \033[1;32mCHECK YOUR URL')
    else:
       req = nabil.get(url)
       bs = bs4.BeautifulSoup(req.text,'html.parser')
       main = bs.find_all('a')
       main_len = len(main)
       print 
       print ('     \033[1;31m[+] \033[1;32mSITE URL    \033[1;31m>> \033[1;33m'+url)
       print ('     \033[1;31m[+] \033[1;32mTOTAL LINKS \033[1;31m>> \033[1;33m'+str(main_len))
       print ('     \033[1;31m[+] \033[1;32mSCANING     \033[1;31m>> \033[1;33mSTARTING....\033[1;32m')
       time.sleep(1.5)
       print
      
       for link in main:
          
           link = link.get("href")
           print (link)
           


def intro():
    os.system('clear')
    print (logo)
    print 
    print ("\033[1;31m[1] \033[1;34m>> \033[1;33mExtract-Links \033[1;31m(Default)")
    print ("\033[1;31m[2] \033[1;34m>> \033[1;33mExtract-Links \033[1;31m(By Using Api)")
    print 
    user_choise = raw_input('\033[1;31m>> \033[1;32mEnter Your Choice : \033[1;33m')
    if user_choise == "1":
       main()
    elif user_choise ==  "2":
         os.system('python2 extract-link-online.py')
    else:
        print ('\033[1;31m[+] Your Choice Not Vailed')

intro()
