#!/usr/bin/python

import os , time
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from optparse import *

class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()



print(cl.red+"""
 _____                               
/  ___|                              
\ `--.  ___  ___ _ __ ___  ___ _   _ 
 `--. \/ _ \/ __| '__/ _ \/ __| | | |
/\__/ /  __/ (__| | |  __/ (__| |_| |
\____/ \___|\___|_|  \___|\___|\__, |
                                __/ |
                               |___/

\t	python encrypter/decrypter by m4xP0wer
\t               

"""+cl.end)

parser = OptionParser("""

#Usage:

	-e   to encrypt files
	-d   to decrypt files
	-p   password to encryption or decryption files

#Example:

	python Secrecy.py -e <Your File> -p <Password>

	python Secrecy.py -d <Your File> -p <Password>


""")

def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = "en" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV =Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

def getKey(password):
            hasher = SHA256.new(password.encode('utf-8'))
            return hasher.digest()

def decrypt(key, filename):
	chunksize = 64 * 1024
	outputFile = filename.split('.hacklab')[0]

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)

def getkey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()

def Main():
	parser.add_option("-e",dest="en",type="string", help="This Option To Encryption Files")
	parser.add_option("-d",dest="de",type="string", help="This Option To Decrytpion Files")
	parser.add_option("-p",dest="password",type="string", help="Enter Password")
	(options, args) = parser.parse_args()
	if options.en == None and options.de == None:
		print(cl.blue+parser.usage+cl.end)
		exit(0)
	else:
		en = str(options.en)
		de = str(options.de)
		password = str(options.password)
		if options.de == None:
			print(cl.red+"[+] Encrypting......"+cl.end)
			encrypt(getkey(password), en)
			time.sleep(1.5)
			print(cl.red+"\n[+] Done"+cl.end)
		elif options.en == None:
			print(cl.red+"[+] Decrypting......"+cl.end)
			decrypt(getkey(password), de)
			time.sleep(1.5)
			print(cl.red+'\n[+] Done'+cl.end)
		else:
			print("Oops operation failed")

if __name__ == '__main__':
	Main()
