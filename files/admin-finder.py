#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import sys
import time
import requests
session = requests.Session()
wordlist = open('paths.txt','r')
os.system('rm -rf found.txt')
#os.system('touch found.txt')
#f = open('found.txt','w')
logo = """ \033[1;94m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/

Created By : \033[1;96mNabil-Rahman \033[1;31m|\033[1;0m [V 1.1.1]

\033[1;32m------------------------------------------
\33[93m AUTHOR  : Cyber_Sixteen 
\33[93m GITHUB  : github.com/Nabil-OfficiaL
\33[93m FB      : nabil.404
\33[93m TYPE    : Admin-Finder
\033[1;32m------------------------------------------
"""


def main():
    os.system('clear')
    print (logo)
    print
    web = raw_input('\033[1;31m>>\033[1;32m Enter Your Url : \033[1;36m')
    req_code = requests.head(web)
    if req_code.status_code != 200:
       print ('URL ERROR PLS CHK !')
    else:
       print 
       for word in wordlist:
           word = word.strip()
          
           req = session.get(web+word)
           if req.status_code == 200:
              print ('\033[1;32m[+] FOUND : ' + web+word)
              os.system('touch found.txt')
              found = web+word
              v = open('found.txt','a')
              f = v.write('[+] '+found+'\n')
              v.close()
            
              
           if web+word == web+"/Admin2015/":
              time.sleep(3)
              os.system('clear')
              print (logo)
              print
              print ('\033[1;31m<<<\033[1;33m FOUNDED URLS \033[1;31m>>>')
            
              print ('\033[1;32m')
              os.system('cat found.txt')
              print
              print ('\033[1;33m   << Thanks For Using >>')

           else:
              print ('\033[1;31m[!] Not Found ' + web+word)
          
          
main()
