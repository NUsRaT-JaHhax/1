#!/usr/bin/python
import os
import time
import sys

dork = open('dork-list.txt','r')
dork2 = open('sqlid.txt','r')
xss_dork = open('xssd.txt','r')
lafid = open('lafid.txt','r')
logo = """ \033[1;94m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/

Created By : \033[1;96mNabil-Rahman \033[1;31m|\033[1;0m [V 1.1.1]

\033[1;32m------------------------------------------
\33[93m AUTHOR  : Team DarkWeb T-D
\33[93m GITHUB  : github.com/Nabil-Official
\33[93m FB      : nabil.404
\33[93m TYPE    : Dork-Generator
\033[1;32m------------------------------------------
"""


def lafi():
    os.system("clear")
    print logo
    print 
    for word4 in lafid:
        word4 = word4.strip()
        print ('\033[1;31m[+] \033[1;32m'+word4)




def xss():
    os.system('clear')
    print logo
    print 
    for word3 in xss_dork:
        word3 = word3.strip()
        print ('\033[1;31m[+] \033[1;32m'+word3)



def sqli1():
    os.system('clear')
    print (logo)
    print
    
    key = raw_input('\033[1;31m[+]\033[1;32m ENTER KEYWORDS :\033[1;36m ')
    while key == "":
          print ("\033[1;31mEx- News,Gellary")
          key = raw_input('\033[1;31m[+]\033[1;32m ENTER KEYWORDS :\033[1;36m ')
           
    else:
        print
        for word in dork:
            word = word.strip()
            print ('\033[1;31m[+]\033[1;32m '+'inurl:'+key+word)
            d = "inurl:"+key+word
            if d == "inurl:news.php?maincat_id=":
               print 
               print ('\033[1;33m   << Thanks For Using >>')



def sqli2():
    os.system('clear')
    print logo
    print 
    for word2 in dork2:
        word2 = word2.strip()
        print ('\033[1;31m[+] \033[1;32minurl:'+word2)

def intro():
    os.system('clear')
    print (logo)
    print 
    print ("\033[1;32m[1]\033[1;31m >>\033[1;36m SQLI \033[1;33m|\033[1;31m With Own Keywords")
    print ("\033[1;32m[2]\033[1;31m >>\033[1;36m SQLI \033[1;33m|\033[1;31m Dorks")
  
    print ("\033[1;32m[3]\033[1;31m >>\033[1;36m XSS \033[1;33m |\033[1;31m Dork & Payloads")

  
    print ("\033[1;32m[4]\033[1;31m >>\033[1;36m LFI \033[1;33m |\033[1;31m Dorks")
  
  
    
    print 
    user = raw_input('\033[1;31m[+]\033[1;32m Enter Your Choice : ')
    if user == "1":
       sqli1()
    elif user == "2":
         sqli2()
    elif user == "3":
         xss()
    elif user == "4":
         lafi()
    else:
         exit()
         print ('<<< Thanks For Using >>>')
intro() 

