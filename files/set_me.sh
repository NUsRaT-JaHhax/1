#!/usr/bin/python2
# coding : utf-8

main () {
clear
echo -en "\033[32m"
figlet SETUP
echo
echo -en "\033[31m[+] \033[32mINSTALLING PKGS \033[31m[+]"
sleep 2 
echo
apt update && apt upgrade
pkg install nmap -y 
echo
echo -en "\033[31m[+] \033[32mINSTALLING PKGS \033[31m[+]"
echo 
sleep 1 
echo "[+] INSTALLING MODULES [+]"
echo
sleep 2
pip2 install requests 
pip2 install mechanize
pip  install urllib2 
pip install threaded
pip install hashlib 
pip install jsonlib
}
main
