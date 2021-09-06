#!/usr/bin/python2 
# -*- coding: utf-8 -*-
# Author : Nabil-Official ! 
import os 
import sys
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
    domain = raw_input('\033[1;31m>> \033[1;32mEnter Domain Name :\033[1;35m ')
    print 
    print ('\033[1;31m[+]\033[1;32m TARGET SITE :\033[1;33m '+domain)
    print ('\033[1;31m[+]\033[1;32m SCANING.....')
    time.sleep(1)
    print ('\033[1;32m')
    try:
       whois = os.system('whois '+domain)
       print (whois)
       print ("     \033[1;31m<<< \033[1;33mThanks For Using \033[1;31m>>>")
       print 
       user = raw_input('\033[1;31m[+] \033[1;34mPRESS ENTER TO BACK MENU\033[1;31m [+]')
       if user == "":
          os.system('cd .. && python2 n-web.py')
    except:
       print ('[+] AN ERROR ACCOURDD')
       #print ('[+] AN ERROR ACCOURD')
       
main()
