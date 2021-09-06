#!/usr/bin/env python
# encoding: utf-8

# __author__ = "F1uYu4n"

import time 
import json
import os
import re
import threading
from urllib import unquote

import requests
from requests.exceptions import RequestException
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


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
os.system('clear')

timeout = 30
retry_cnt = 2
common_headers = {u"User-Agent": u"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

print (logo)
# md5-16, md5-32, sha1, mysql-323, mysql5, ...
def cmd5(passwd):
    url = u"https://cmd5.com/"
    try_cnt = 0
    while True:
        try:
            s = requests.Session()
            req = s.get(url, headers=common_headers, timeout=timeout, verify=False)
            __ = dict(re.findall(ur'id="(.+?)" value="(.*?)"', req.text))

            headers = dict(common_headers, **{u"Referer": url})
            data = {u"__EVENTTARGET": __[u"__EVENTTARGET"], u"__EVENTARGUMENT": __[u"__EVENTARGUMENT"],
                    u"__VIEWSTATE": __[u"__VIEWSTATE"], u"__VIEWSTATEGENERATOR": __[u"__VIEWSTATEGENERATOR"],
                    u"ctl00$ContentPlaceHolder1$TextBoxInput": passwd,
                    u"ctl00$ContentPlaceHolder1$InputHashType": u"md5",
                    u"ctl00$ContentPlaceHolder1$Button1": u"\u67e5\u8be2",
                    u"ctl00$ContentPlaceHolder1$HiddenFieldAliCode": u"",
                    u"ctl00$ContentPlaceHolder1$HiddenField1": u"",
                    u"ctl00$ContentPlaceHolder1$HiddenField2": __[u"ctl00_ContentPlaceHolder1_HiddenField2"]}
            req = s.post(url, headers=headers, data=data, timeout=timeout, verify=False)
            result = re.findall(ur'<span id="LabelAnswer" class="LabelAnswer".*?>(.+?)<', req.text)[0]
            print u"\033[1;31m[*]\033[1;32m DATA-BASE-1 : {0}".format(re.sub(ur"\u3002.*", u"", result))
            break
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"\033[1;31m[-] DATA-BASE-1 : RequestError"
                break
        except (KeyError, IndexError), e:
            print u"\033[1;31m[-] DATA-BASE-1 : Error: {0}".format(e)
            break


# md5-16, md5-32
def pmd5(passwd):
    url = u"https://api.pmd5.com/pmd5api/"
    try_cnt = 0
    while True:
        try:
            s = requests.Session()
            req = s.get(u"{0}checkcode".format(url), headers=common_headers, timeout=timeout, verify=False)
            pmd5api = re.findall(ur"koa.sess.pmd5api=([\w=]+)", req.headers[u"Set-Cookie"])
            if pmd5api:
                capcha = json.loads(pmd5api[0].decode("base64"))[u"capcha"]
                params = {u"checkcode": capcha, u"pwd": passwd}
                req = s.get(u"{0}pmd5".format(url), params=params, headers=common_headers, timeout=timeout,
                            verify=False)
                result = req.json()[u"result"].values()
                if result:
                    print u"\033[1;31m[+] \033[1;32mDATA-BASE-2 : {0}".format(result[0])
                else:
                    print u"\033[1;31m[-] DATA-BASE-2 : NotFound"
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"\033[1;31[-] pmd5: RequestError"
                break
        except (KeyError, IndexError), e:
            print u"[-] DATA-BASE-2 : Error: {0}".format(e)
            break


# md5-16, md5-32
def xmd5(passwd):
    url = u"https://xmd5.com/"
    try_cnt = 0
    while True:
        try:
            s = requests.Session()
            data = {u"UserName": u"jevoyf46098@chacuo.net", u"Password": u"eEZT1FaD&$S*!t3!Y2d0",
                    u"logins": u"\u767b\u5f55"}
            req = s.post(u"{0}user/CheckLog.asp".format(url), headers=common_headers, data=data, timeout=timeout,
                         verify=False)
            checkcode = re.findall(ur'checkcode2 type=hidden value="(.+?)">', req.text)[0]

            params = {u"hash": passwd, u"xmd5": u"MD5 \u89e3\u5bc6", u"open": u"on", u"checkcode2": checkcode}
            headers = dict(common_headers, **{u"Referer": url})
            req = s.get(u"{0}md5/search.asp".format(url), params=params, headers=headers, timeout=timeout,
                        allow_redirects=False, verify=False)
            location = req.headers[u"Location"]
            if location == u"getpass.asp?type=no":
                print u"[-] xmd5: NotFound"
            elif location[:16] == u"getpass.asp?info":
                print u"[+] xmd5: {0}".format(location[17:])
            elif location.find(u"403.asp") > 0:
                print u"[-] xmd5: checkcode error!"
            else:
                print u"[+] xmd5: Pay to get plain."
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"[-] xmd5: RequestError"
                break
        except IndexError, e:
            print u"[-] xmd5: Error: {0}".format(e)
            break


# md5-16, md5-32, sha1
def navisec(passwd):
    url = u"https://md5.navisec.it/"
    try_cnt = 0
    while True:
        try:
            s = requests.Session()
            req = s.get(url, headers=common_headers, timeout=timeout, verify=False)
            _token = re.findall(ur'name="_token" value="(.+?)">', req.text)[0]

            headers = dict(common_headers, **{u"Referer": url})
            data = {u"_token": _token, u"hash": passwd}
            req = s.post(u"{0}search".format(url), headers=headers, data=data, timeout=timeout, verify=False)
            rsp = req.text
            result = re.findall(ur"<code>(.*?)</code>", rsp)[0]
            num = re.findall(ur"\u79ef\u5206\u5269\u4f59\uff1a[-]?\d+", rsp)[0]
            if result.find(u"\u672a\u80fd\u89e3\u5bc6") >= 0:
                print u"[-] navisec: {0}{1}".format(result, num)
            else:
                print u"[+] navisec: {0} {1}".format(result, num)
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"[-] navisec: RequestError"
                break
        except IndexError, e:
            print u"[-] navisec: Error: {0}".format(e)
            break


# md5-32, sha1, sha256, sha384, sha512
def hashtoolkit(passwd):
    url = u"https://hashtoolkit.com/reverse-hash/"
    try_cnt = 0
    while True:
        try:
            params = {u"hash": passwd}
            req = requests.get(url, headers=common_headers, params=params, timeout=timeout, verify=False)
            rsp = req.text
            if rsp.find(u"No hashes found for") > 0:
                print u"[-] hashtoolkit: NotFound"
            else:
                plain = re.findall(r'<a href="/generate-hash/\?text=(.*?)"', rsp, re.S)[0]
                print u"\033[1;31m[+] \033[1;32mDATA-BASE-3 : {0}".format(unquote(plain))
                break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"[-] hashtoolkit: RequestError"
                break
        except IndexError, e:
             print u"\033[1;31m[-] DATA-BASE-3 : {0}".format(e)
             break


# md5-32
def nitrxgen(passwd):
    url = u"http://www.nitrxgen.net/md5db/"
    try_cnt = 0
    while True:
        try:
            req = requests.get(u"{0}{1}.txt".format(url, passwd), headers=common_headers, timeout=timeout)
            rsp = req.text
            if rsp:
                print u"\033[1;31m[+]\033[1;32m DATA-BASE-4 : {0}".format(rsp)
                
              
            else:
                print u"\033[1;31m[-] DATA-BASE-4 : NotFound"
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"\033[1;31m[-] DATA-BASE-4 : RequestError"
                break


# md5-32
def myaddr(passwd):
    url = u"http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"
    try_cnt = 0
    while True:
        try:
            data = {u"md5": passwd}
            req = requests.post(url, headers=common_headers, data=data, timeout=timeout)
            result = re.findall(r"Hashed string</span>:\s(.+?)</div>", req.text)
            if result:
                print u"\033[1;31m[+]\033[1;32m DATA-BASE-5 : {0}".format(result[0])
            else:
                print u"\033[1;31m[-] DATA-BASE-5 : NotFound"
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"\033[1;31m[-] DATA-BASE-5 : RequestError"
                break





# md5-32
def gromweb(passwd):
    url = u"https://md5.gromweb.com/"
    try_cnt = 0
    while True:
        try:
            params = {u"md5": passwd}
            req = requests.get(url, headers=common_headers, params=params, timeout=timeout, verify=False)
            rsp = req.text
            if rsp.find(u"succesfully reversed") > 0:
                plain = re.findall(ur'<em class="long-content string">(.*?)</em>', rsp)[0]
                print u"\033[1;31m[+]\033[1;32m DATA-BASE-6 : {0}".format(plain)
            else:
                print u"\033[1;31m[-] DATA-BASE-6 : NotFound"
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"\033[1;31m[-] DATA-BASE-6 : RequestError"
                break
        except IndexError, e:
            print u"\033[1;31m[-] DATA-BASE-6 : Error: {0}".format(e)
            break



# md5-16, md5-32
def tellyou(passwd):
    url = u"http://md5.tellyou.top/MD5Service.asmx/HelloMd5"
    try_cnt = 0
    while True:
        try:
            params = {u"Ciphertext": passwd}
            headers = dict(common_headers, **{u"X-Forwarded-For": u"192.168.1.1"})
            req = requests.get(url, params=params, headers=headers, timeout=timeout)
            result = re.findall(ur'<string xmlns="http://tempuri.org/">(.*?)</string>', req.text)
            if result:
                print u"\033[1;31m[+] \033[1;32mDATA-BASE-7 : {0}".format(result[0])
            else:
                print u"\033[1;31m[-] DATA-BASE-7 : NotFound"
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"\033[1;31m[-] tellyou: RequestError"
                break
        except IndexError, e:
            print u"[\033[1;31m-] DATA-BASE-7 : Error: {0}".format(e)
            break


# md5-16, md5-32, sha1, mysql-323, mysql5, ...
def ttmd5(passwd):
    url = u"http://www.ttmd5.com/do.php"
    try_cnt = 0
    while True:
        try:
            s = requests.Session()
            params = {u"c": u"User", u"m": u"doLogin"}
            data = {u"hidUser": u"uplnwkdc@mail.bccto.me", u"hidPassword": u"c927dc915426c2c89de3330c397fadf9"}
            s.post(url, headers=common_headers, params=params, data=data, timeout=timeout)

            params = {u"c": u"Decode", u"m": u"getMD5", u"md5": passwd}
            req = s.get(url, headers=common_headers, params=params, timeout=timeout)
            rsp = req.json()
            if u"plain" in rsp:
                print u"\033[1;31m[+]\033[1;32m DATA-BASE-8 : {0}".format(rsp[u"plain"])
            else:
                print u"\033[1;31m[-] DATA-BASE-8 : NotFound"
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"\033[1;31m[-] DATA-BASE-8 : RequestError"
                break
        except IndexError, e:
            print u"\033[1;31m[-] DATA-BASE-8 : Error: {0}".format(e)
            break


# mysql5
def mysql_password(passwd):
    url = u"https://www.mysql-password.com/api/get-password"
    try_cnt = 0
    while True:
        try:
            data = {u"hash": passwd}
            req = requests.post(url, headers=common_headers, data=data, timeout=timeout, verify=False)
            result = req.json()
            if u"error" in result:
                print u"[-] mysql_password: {0}".format(result[u"error"])
            else:
                print u"[+] mysql_password: {0}".format(result[u"password"])
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print u"[-] mysql_password: RequestError"
                break
        except IndexError, e:
            print u"[-] mysql_password: Error: {0}".format(e)
            break


def crack(passwd):
    threads = [threading.Thread(target=cmd5, args=(passwd,)), threading.Thread(target=hashtoolkit, args=(passwd,)),
               threading.Thread(target=ttmd5, args=(passwd,))]
    if len(passwd) == 41 and re.match(r'\*[0-9a-f]{40}|\*[0-9A-F]{40}', passwd):
        threads.append(threading.Thread(target=chamd5, args=(passwd[1:], u"300",)))
        threads.append(threading.Thread(target=mysql_password, args=(passwd,)))
    elif len(passwd) == 40 and re.match(r'[0-9a-f]{40}|[0-9A-F]{40}', passwd):
        threads.append(threading.Thread(target=navisec, args=(passwd,)))
        threads.append(threading.Thread(target=chamd5, args=(passwd, u"100",)))
        threads.append(threading.Thread(target=chamd5, args=(passwd, u"300",)))
        threads.append(threading.Thread(target=mysql_password, args=(passwd,)))
    elif len(passwd) == 32 and re.match(r'[0-9a-f]{32}|[0-9A-F]{32}', passwd):
        threads.append(threading.Thread(target=pmd5, args=(passwd,)))
     #   threads.append(threading.Thread(target=xmd5, args=(passwd,)))
      #  threads.append(threading.Thread(target=navisec, args=(passwd,)))
        threads.append(threading.Thread(target=nitrxgen, args=(passwd,)))
        threads.append(threading.Thread(target=myaddr, args=(passwd,)))
    #   . threads.append(threading.Thread(target=chamd5, args=(passwd, u"md5",)))
        threads.append(threading.Thread(target=gromweb, args=(passwd,)))
       # threads.append(threading.Thread(target=bugbank, args=(passwd,)))
        threads.append(threading.Thread(target=tellyou, args=(passwd,)))
    elif len(passwd) == 16 and re.match(r'[0-9a-f]{16}|[0-9A-F]{16}', passwd):
        threads.append(threading.Thread(target=pmd5, args=(passwd,)))
        #threads.append(threading.Thread(target=xmd5, args=(passwd,)))
       # threads.append(threading.Thread(target=navisec, args=(passwd,)))
       # threads.append(threading.Thread(target=chamd5, args=(passwd, u"md5",)))
        #threads.append(threading.Thread(target=chamd5, args=(passwd, u"200",)))
        #threads.append(threading.Thread(target=bugbank, args=(passwd,)))
        threads.append(threading.Thread(target=tellyou, args=(passwd,)))
    elif passwd.find(':') > 0:
        threads.append(threading.Thread(target=chamd5, args=(passwd, u"10",)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()


def main():
    x = 1
    while x == 1:
        x = x+1 
        try:
            passwd = raw_input(u"Hash: \033[1;35m").strip()
            print 
            print ('\033[1;31m>>\033[1;32m YOUR HASH : \033[1;33m'+passwd)
            print ('\033[1;31m>>\033[1;32m START CRACKING....')
            time.sleep(2)
            print 
            print ('\033[1;34m------------------------------')
            if passwd:
                with open("{0}\\hash.log".format(os.path.split(os.path.realpath(__file__))[0]), 'a+') as f:
                    f.write(passwd + os.linesep)
                crack(passwd)
            print ('\033[1;34m------------------------------')
        except (KeyboardInterrupt, ValueError, EOFError):
            break
        print 
        print ('\033[1;31m<<< \033[1;33mTHANKS FOR USING \033[31m>>> ')

if __name__ == '__main__':
    main()
