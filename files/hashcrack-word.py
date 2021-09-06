import hashlib
import os 
os.system('clear')
#banner
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
print (logo)
print 
wlist=input("\033[1;31m>> \033[1;32mWordlist : \033[1;33m")
hash2crack=input("\033[1;31m>> \033[1;32mHash : \033[1;33m")

#read file
wlistlines=open(wlist, "r").readlines()

#loop
for i in range(0, len(wlistlines)):
    hash2comp=hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
    if hash2crack == hash2comp:
        print 
        print("\033[1;31m[+] \033[1;32mFound :  "+wlistlines[i].replace("\n",""))
        exit()
print("[+] Not Found")
