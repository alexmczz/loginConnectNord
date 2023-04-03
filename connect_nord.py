import os
import time
import webbrowser
import requests
import re
import subprocess

def get_nord_login():
    os.system('nordvpn login > vpnAuth.txt')
    output = subprocess.check_output('cat vpnAuth.txt', shell=True)
    text = output.decode()
    pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(pattern, text)

    if match:
        url = match.group()
        response = requests.get(url)
        webbrowser.open(response.url)
    else:
        print('Invalid URL')
        for i in range(5):
            time.sleep(1)
            print(i)
            get_nord_login()


def connect():
	res = input('##Press Enter To connec(Quit to exit)t##')
	if res == '':
		os.system('nordvpn connect')
	elif res.upper() == 'QUIT':
		print('Quitting...')
		for i in range(5):
			time.sleep(1)
	else:
		return connect()
 
get_nord_login()
connect()