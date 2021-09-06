#!/usr/bin/python2 
# -*- coding: utf-8 -*-
# Author : Nabil-Rahman 

import urllib2 
import os,sys
import json 
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
    domain = raw_input('\033[1;31m>> \033[1;32mEnter IP/DOMAIN : \033[1;35m')
    print 
    if domain == "":
       print ('\033[1;31m[+] Enter Domain Or IP to Scan ! ')
    else:
      
       print ("  \033[1;31m>>> \033[1;32mT4GET   : \033[1;33m"+domain)
       print ("  \033[1;31m>>> \033[1;32mSCANING : \033[1;33mSTARTING....")
       print 
       time.sleep(1)
       url = "http://ip-api.com/json/"
       req = urllib2.urlopen(url+domain)
       r = req.read()
       js = json.loads(r)
       print ("\033[1;31m[+] \033[1;33mIP      : \033[1;32m"+js["query"])
       print ("\033[1;31m[+] \033[1;33mCOUNTRY : \033[1;32m"+js["country"])
       print ("\033[1;31m[+] \033[1;33mCITY    : \033[1;32m"+js["city"] )
       print ("\033[1;31m[+] \033[1;33mLAT     : \033[1;32m"+str(js["lat"]))
       print ("\033[1;31m[+] \033[1;33mLON     : \033[1;32m"+str(js["lon"]))
       print ("\033[1;31m[+] \033[1;33mISP     : \033[1;32m"+js["isp"])
       print ("\033[1;31m[+] \033[1;33mORG     : \033[1;32m"+js["org"])
       print ("\033[1;31m[+] \033[1;33mAS      : \033[1;32m"+js["as"])
       print 
       print ('  \033[1;31m<<< \033[1;33mThanks For Using \033[1;31m>>>')
       
       print 
       user = raw_input('\033[1;31m[+] \033[1;34mPRESS ENTER TO GO BACK MENU \033[1;31m[+]')
    
       print 
       if user == "":
          os.system('cd .. && python2 n-web.py')
main()
