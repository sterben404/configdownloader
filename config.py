#!/usr/bin/python2.7
#Author By Sterben404
#Tools ini berfungsi untuk mendownload configuration pada website
#atau bisa juga di gunakan untuk mendownload file yang berformat (.txt) secara massal
#Inspired tools by Bedz
#ExtreameInInformationTechnology(EXI2T Cyber Team)
#CopyRight-2019
#Install wget terlebih dahulu
#Note:Tools Ini tidak berfungsi untuk web HTTPS yang tidak mempunyai Certificate Secure
import os,re,sys,time
import requests,urllib
import random
import threading
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[96m'
purple = '\033[95m'
reset = '\033[0m'
os.system('clear')

print "" ,red
print("____ ____ _  _ ____ _ ____ ")
print(yellow+"|    |  | |\ | |___ | | __ ")
print(green+"|___ |__| | \| |    | |__] ")
print(red+"Downloader by %s Sterben404" % green)
print(blue+"Masukan Link Config%s(example: http://www.web.com/folder_config/)" % red)

def write(s):
		for c in s + '\n':
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(random.random() * 0.02)
def cekdir():
	try:
		os.makedirs(folder)
	except OSError, x:
		write(red + "[!] Folder Sudah Ada" + reset)
		exit()

def main(url):
	os.chdir(folder)
	r = requests.get(link)
	url = re.findall('"[^>"]+.txt"',r.text)
	for config in url:
		os.system('wget --no-check-certificate -q '+link+config)
		write("[%s+%s] Sedang Mendownload Config %s %s %s" % (green,reset,purple,config,reset))

if __name__ == "__main__":
	url = raw_input(yellow + 'Link Config: ' + reset)
	erurl = '/'
	folder = raw_input(yellow + 'Folder Untuk Config: ' + reset)
	cekdir()
	link = url+erurl
	t = threading.Thread(target=main, args=(link, )).start()
