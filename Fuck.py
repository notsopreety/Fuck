#!/usr/bin/python

# coding=utf-8

# Originally Written By: Samir Badaila

# Source : Python2"

# Donot Recode It. 

#Import module

try:

    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests

    from multiprocessing.pool import ThreadPool

    from requests.exceptions import ConnectionError

    from mechanize import Browser

except ImportError:

    os.system('pip2 install requests')

    os.system('pip2 install mechanize')

    os.system('python2 Fuck.py')

#Browser Setting

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():

	print "[!] Exit"	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def hamza(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.03)

##### LOGO #####

banner ="""

\033[1;94m ## ##     ##     ##   ##    ####   ### ##   

\033[1;92m##   ##     ##     ## ##      ##     ##  ##  

\033[1;93m####      ## ##   # ### #     ##     ##  ##  

\033[1;95m #####    ##  ##  ## # ##     ##     ## ##   

\033[1;94m    ###   ## ###  ##   ##     ##     ## ##   

\033[1;96m##   ##   ##  ##  ##   ##     ##     ##  ##

\033[1;97m ## ##   ###  ##  ##   ##    ####   #### ##  

 \033[37;1m[\033[41;1m FACEBOOK ACCOUNT CLONING \033[00;1m\033[37;1m ]\n

 \033[32;1mCreator \033[37;1m: \033[33;1mSamir-Badaila

 \033[32;1mVersion \033[37;1m: \033[33;1m1.2

"""

hammad="""

\033[1;91m  _____           _     __   __          

\033[1;92m |  ___|   _  ___| | __ \ \ / /__  _   _ 

\033[1;93m | |_ | | | |/ __| |/ /  \ V / _ \| | | |

\033[1;94m |  _|| |_| | (__|   <    | | (_) | |_| |

\033[1;95m |_|   \__,_|\___|_|\_\   |_|\___/ \__,_|
\033[1;95m=========================================

\033[1;96m| || | __ _  _ __   _ __   __ _  __| |

\033[1;97m| __ |/ _` || '  \ | '  \ / _` |/ _` |

\033[1;91m|_||_|\__/_||_|_|_||_|_|_|\__/_|\__/_|

"""

# titik #

def tik():

	titik = [".   ","..  ","... "]

	for o in titik:

		print("\r[✔] Logging In "+o),;sys.stdout.flush();time.sleep(1)

back = 0

id = []

def tlogin():

	os.system('clear')

	print banner

	username = raw_input("[+] TOOL USERNAME: ")

	if username =="Samir":

	    os.system('clear')

	    print banner

	    print "[✓] TOOL USERNAME: "+username+ " (correct)"

	else:

	    print "[!] Invalid Username."

	    time.sleep(1)

	    tlogin()

	    

	passw = raw_input("[+] TOOL PASSWORD: ")

	if passw =="Notsopreety":

	    os.system('clear')

	    print banner

	    print "[✓] TOOL USERNAME: " +username+ " (correct)"

	    print "[✓] TOOL PASSWORD: " +passw+ "  (correct)"

	    time.sleep(2)

	else:

	    print "[!] Invalid Password."

	    time.sleep(1)

	    tlogin()

	try:

		toket = open('login.txt','r')

		os.system('python2 Syco.py')

	except (KeyError,IOError):

		methodlogin()

	else:

		print "[!] Invalid Password"

		time.sleep(1)

		tlogin()

##### Login Method #####

def methodlogin():

	os.system('clear')

	print banner

	print "[1] Login With ID/Password."

	print "[2] Login Using Token."

        print "[3] Cloning Without Login."

	print "[0] Exit."

	print ('      ')

	hos = raw_input("\nChoose Option >>  ")

	if hos =="":

		print"[!]  Wrong Input"

		exit()

	elif hos =="1":

		login()

	elif hos =="2":

		os.system('clear')

		print banner

		hosp = raw_input("[+] Give Token : ")

		tik()

		hopa = open('login.txt','w')

		hopa.write(hosp)

		hopa.close()

		print "\n[✓] Logged In Successfully."

		time.sleep(1)

		os.system('python2 Syco.py')

	

	elif hos =="3":

		os.system('clear')

		print banner

                print hammad

		hamza('[✓] Please Wait While Tool Is Loading')

		hamza('=====>>>>>>-10%...')

	        hamza('=======>>>>>>-20%...')

                hamza('=========>>>>>>-30%...')

                hamza('===========>>>>>>-40%...')

	        hamza('=============>>>>>>-50%...')

                hamza('===============>>>>>>-60%...')

                hamza('=================>>>>>>-70%...')

	        hamza('===================>>>>>>-80%...')

                hamza('=====================>>>>>>-90%...')

                hamza('=======================>>>>>>-100%...')

                hamza('Samir The Great Is Here To Fuck Down The Whole System')

		time.sleep(3)

                os.system("clear")

		os.system("python2 Hammad.py")

		

	elif hos =="0":

		exit()

	else:

		print"[!] Wrong Input"

		exit()

def login():

	os.system("clear")

	try:

		tb=open('login.txt', 'r')

		os.system("python2 Syco.py")

	except (KeyError,IOError):

		os.system("clear")

		print (banner)

		hamza('[!] MR- ROBOT PROGRAMING')

		hamza('[!] Use a New Facebook Account To Login')

		print'-------------------------------------'

		iid=raw_input('[+] Number/Email: ')

		id=iid.replace(" ","")

		pwd=raw_input('[+] Password : ')

		tik()

		data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

		z=json.load(data)

		if 'access_token' in z:

		    st = open("login.txt", "w")

		    st.write(z["access_token"])

		    st.close()

		    print "\n[✓] Logged In Successfully."

		    time.sleep(1)

		    os.system("clear")

		    os.system("python2 Syco.py")

		else:

		    if "www.facebook.com" in z["error_msg"]:

		        print ('[!] User Must Verify Account Before Login.')

		        time.sleep(3)

		        login()

		    else:

		        print ('[!]Number/User Id/ Password Is Wrong !')

		        time.sleep(1)

		        login()

if __name__=='__main__':

    tlogin()
