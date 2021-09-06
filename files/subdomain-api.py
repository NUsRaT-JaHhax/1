#!/usr/bin/python2
# -*- coding: utf-8 -*-
# Author : Nabil-Rahman

import requests as nabil 
import os,sys,time 

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

def intro():
    os.system('clear')
    print (logo)
    print 
    domain = raw_input('\033[1;31m>> \033[1;32mEnter Domain Name : \033[1;35m')
    time.sleep(0.5)
    print 
    print ('     \033[1;31m>> \033[1;32mTARGET : \033[1;33m'+domain)
    print ('     \033[1;31m>> \033[1;32mSCANNING......')
    print ('     \033[1;31m>> \033[1;32mNOTE : \033[1;31mIf You Face Any Problem While Scanning Use VPN')
    time.sleep(2.5)
    
    print ('\033[1;32m')
    print 
    url = "https://api.hackertarget.com/hostsearch/?q="+domain 
    try:
       req = nabil.get(url)
       re = req.text 
       print (re)
       print 
       print ('  \033[1;31m<<< \033[1;33mThanks For Using \033[1;31m>>>')
       print
       user = raw_input('\033[1;31m[+] \033[1;34mPRESS ENTER TO GO BACK MENU \033[1;31m[+]')           

       print
       if user == "":
          os.system('cd .. && python2 n-web.py')
    except:
       print ('\033[1;31m[+] Something Is Wrong ! ')



def main():
    os.system('clear')
    print (logo)
    print 
    print ('\033[1;31m[1] \033[1;34m>> \033[1;32mSub-Domain-Lookup \033[1;31m(Using API)')
    print ('\033[1;31m[2] \033[1;34m>> \033[1;32mSub-Domain-Lookup \033[1;31m(Default)')
    print 
    user_choice = raw_input('\033[1;31m>> \033[1;33mEnter Your Choice : \033[1;36m')
    if user_choice == "1":
       intro()
    elif user_choice == "2":
         os.system('python sub-domain.py')
    else:
       print ('\033[1;31m[+] Input Correctly')
main()




