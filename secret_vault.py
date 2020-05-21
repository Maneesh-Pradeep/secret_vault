#!/usr/bin/env python
import os
import base64
import shutil
import pyAesCrypt
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class secret_vault:
	
	buffer_size = 64 * 1024

	def __init__(self, masterpwd):
		self.masterpwd = masterpwd

	def add_file(self, path, encrypt):
		if encrypt:
			filenameWithExt = os.path.basename(path) + '.aes'
			vaultpath = self.hid_dir + filenameWithExt
			pyAesCrypt.encryptFile(path, vaultpath, self.key.decode(), self.buffer_size)
		else:
			shutil.copy(path, self.hid_dir)

	def del_file(self, index):
		filenameWithExt = self.files[index]
		vaultpath = self.hid_dir + filenameWithExt
		if filenameWithExt.endswith('.aes'):
			filename = filenameWithExt[:-4]
			pyAesCrypt.decryptFile(vaultpath, filename, self.key.decode(), self.buffer_size)
			os.remove(vaultpath)
		else:
			shutil.copy(vaultpath, filenameWithExt)
			os.remove(vaultpath)

	def list_files(self):
		self.get_files()
		if not self.files:
			print("\nVault is empty!!!")
			return
		maxlen = max([len(x) for x in self.files])
		print('')
		print('-'*(maxlen+10))
		print("index\t|files")
		print('-'*(maxlen+10))
		for i, file in enumerate(self.files):
			print("{}\t|{}".format(i, file))
			print('-'*(maxlen+10))

	def generate_key(self, salt=b"\xb9\x1f|}'S\xa1\x96\xeb\x154\x04\x88\xf3\xdf\x05", length=32):
	    password = self.masterpwd.encode()
	    
	    kdf = PBKDF2HMAC(algorithm = hashes.SHA256(),
	                     length = length,
	                     salt = salt,
	                     iterations = 100000,
	                     backend = default_backend())
	    
	    self.key = base64.urlsafe_b64encode(kdf.derive(password))

	def get_files(self):
		self.files = os.listdir(self.hid_dir)

	def set_hid_dir(self, path):
		self.hid_dir = path + '/'

if __name__ == '__main__':
	print("Welcome to the secret vault!!!")
	path = os.path.expanduser('~/.vaultcfg')
	if os.path.exists(path):
		masterpwd = getpass("Enter your Master Password : ")
		vault = secret_vault(masterpwd)
		vault.generate_key()
		fernet = Fernet(vault.key)
		with open(path, 'rb') as f:
			actual_mpwd = f.read()
			try:
				fernet.decrypt(actual_mpwd)
				print('Welcome Back')
			except:
				print("Wrong Master Password!")
				exit()
	else:
		masterpwd = getpass("Create a Master Password : ")
		vault = secret_vault(masterpwd)
		vault.generate_key()
		fernet = Fernet(vault.key)
		enc_mpwd = fernet.encrypt(masterpwd.encode())
		with open(path, 'wb') as f:
			f.write(enc_mpwd)
		path = '~/.vault'
		hid_path = os.path.expanduser(path)
		try:
			os.makedirs(hid_path)
		except FileExistsError:
			pass
		print("Welcome")

	path = '~/.vault'
	hid_path = os.path.expanduser(path)
	vault.set_hid_dir(hid_path)

	choice = 0
	while choice != 4:
		print("\nEnter 1 to hide a file\nEnter 2 to unhide a file\nEnter 3 to view hidden files\nEnter 4 to Exit\nEnter 5 to Reset the vault and delete all of its contents\n")
		try:
			choice = int(input("Enter your choice : "))
		except:
			print("\nUnknown value!")
			continue

		if choice == 1:
			print("\nTip : Drag and Drop the file")
			filepath = input("Enter the path of the file to hide : ")
			filepath = filepath.replace('\\', '')
			if filepath.endswith(' '):
				filepath = filepath[:-1]
			if os.path.exists(filepath):
				if os.path.isfile(filepath):
					while True:
						enc_or_not = input("Do you want to encrypt the file? (Y or N) : ")
						if enc_or_not == 'y' or enc_or_not == 'Y':
							print('\nAdding file to the vault...')
							vault.add_file(filepath, 1)
							print("\nFile successfully added to the vault")
							print("You can now delete the original file if you want")
							break
						elif enc_or_not == 'n' or enc_or_not == 'N':
							print('\nAdding file to the vault...')
							vault.add_file(filepath, 0)
							print("\nFile successfully added to the vault")
							print("You can now delete the original file if you want")
							break
						else:
							print("Type Y or N")
				else:
					print("\nGiven path is a directory and not a file!")
			else:
				print('\nFile does not exists!')

		elif choice == 2:
			print('')
			try:
				file = int(input("Enter the index of the file from view hidden files : "))
				vault.del_file(file)
				print('\nFile unhided successfully')
				print('The file will be present in {}'.format(os.getcwd()))
			except:
				print("\nInvalid index!")

		elif choice == 3:
			vault.list_files()

		elif choice == 5:
			while True:
				confirm = input("\nDo you really want to delete and reset the vault?(Y or N) : ")
				if confirm == 'y' or confirm == 'Y':
					pwdCheck = getpass("\nEnter the password to confirm : ")
					reset = secret_vault(pwdCheck)
					reset.generate_key()
					resetFernet = Fernet(reset.key)
					path = os.path.expanduser('~/.vaultcfg')
					with open(path, 'rb') as f:
						actual_mpwd = f.read()
						try:
							resetFernet.decrypt(actual_mpwd)
							print('Removing and resetting all data...')
							path = os.path.expanduser('~/.vaultcfg')
							os.remove(path)
							shutil.rmtree(vault.hid_dir[:-1])
							print('\nReset done. Thank You')
							exit()
						except Exception as e:
							print(e)
							print("\nWrong Master Password!")
							print("Closing program now...")
							exit()
				elif confirm == 'n' or confirm == 'N':
					print("\nHappy for that")
					break
				else:
					print("Type Y or N")