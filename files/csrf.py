#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os 
import sys 
import time 
#import re


logo = """ \033[1;94m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/\033[1;31m(Pentesting)

Created By : \033[1;96mNabil-Rahman |\033[1;0m [V 1.1.1]

\033[1;32m------------------------------------------
\33[93m AUTHOR  : Team DarkWeb T-D
\33[93m GITHUB  : github.com/Nabil-Official
\33[93m FB      : nabil.404
\033[1;32m--------------------------------------
"""

def main():
    os.system('clear')
    print (logo)
    print  
    domain = raw_input('\033[1;31m>> \033[1;32mEnter Domain Name : \033[1;35m')
    if domain == "":
       print ('\033[1;31m[+] Enter A Domain To Scan')
    else:
       print 
       print ('   \033[1;31m[+] \033[1;32mTARGET   \033[1;31m>> \033[1;33m'+domain)
  
       print ('   \033[1;31m[+] \033[1;32mSCANNING \033[1;31m>> \033[1;33mStarting....')
       time.sleep(2)
       print ("\033[1;32m")
       try:
          out_put = os.system('nmap -p80 --script http-csrf.nse '+domain+" | grep '|_http-csrf:'")
        
          print (out_put)
          print ('  \033[1;31m<<< \033[1;33mThanks For Using \033[1;31m>>>')

          print
          user = raw_input('\033[1;31m[+] \033[1;34mPRESS ENTER TO GO BACK MENU \033[1;31m[+]')           

          print
          if user == "":
             os.system('cd .. && python2 n-web.py')
      
       except:
           print ('\033[1;31m[+] Something Went Wrong ! ')
         
main()



