#!/usr/bin/python2
# -*- coding: utf-8 -*-
# Author : Nabil-Rahman 

import os,sys,time,socket
import requests as nabil



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
    domain = raw_input('\033[1;31m>> \033[1;32mEnter Domain Name : \033[1;35m')
    print 
    print ("     \033[1;31m> \033[1;32mT4GET : \033[1;33m"+domain)
    time.sleep(0.5)
    print ("     \033[1;31m> \033[1;32mSCANING......")
    time.sleep(0.5)
    print ("     \033[1;31m> \033[1;32mNOTE : \033[1;31mIf You Face Any Problem While Scaning Use VPN")
    print 
    time.sleep(3)
    print ("       \033[1;31m<<< \033[1;33mDNS LOOKUP \033[1;31m>>>  ")
    print ("\033[1;32m")
    #3print ('\033[1;32m')
    
    os.system('host '+domain)
    os.system('host -t ns '+domain)
    os.system('host -t TXT '+domain)
    os.system('host -t SOA '+domain)
    print 
    
    print ('      \033[1;31m<<< \033[1;33mReverse Ip Lookup \033[1;31m>>>')
    time.sleep(1.2)
    print ("\033[1;32m")
    try:
      url = "https://api.hackertarget.com/reverseiplookup/?q="+domain
      req = nabil.get(url)
      read = req.text 
      print (read)
  
    except:
       print ('\033[1;31m[+] An Error')
       print 
    print "      \033[1;31m<<< \033[1;33mZONE TRANSFER \033[1;31m>>>"
    time.sleep(0.5)
    print ("\033[1;32m")
  
    url_2 = "https://api.hackertarget.com/zonetransfer/?q="+domain
    req_2 = nabil.get(url_2)
    read_2 = req_2.text
    print (read_2)
    print
    print ('       \033[1;31m<<< \033[1;33mHTTP HEADERS \033[1;31m>>>')
    print ("\033[1;32m")
    time.sleep(1.2)
    url_3 = "https://api.hackertarget.com/httpheaders/?q="+domain
    req_3 = nabil.get(url_3)
    time.sleep(0.5)
    read_3 = req_3.text 
    print (read_3)
    print 
    print ("       \033[1;31m<<< \033[1;33mSUBNET L0OKUP \033[1;31m>>>")
    time.sleep(0.5)
    print ("\033[1;32m")
    url_4 = "https://api.hackertarget.com/subnetcalc/?q="+domain 
    req_4 = nabil.get(url_4)
    read_4 = req_4.text 
    print (read_4)
    print 
    print ('  \033[1;31m<<< \033[1;33mThanks For Using \033[1;31m>>>')

    print
    user = raw_input('\033[1;31m[+] \033[1;34mPRESS ENTER TO GO BACK MENU \033[1;31m[+]')           

    print
    if user == "":
       os.system('cd .. && python2 n-web.py')
main()
