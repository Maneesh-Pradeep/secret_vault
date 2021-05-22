# Secret Vault
A secret file storage vault in python with AES encryption support. 

[![Support me!](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/maneeshpradeep)

## Features
* Store and encrypt your files in an hidden directory somewhere in your PC.
* The freedom to choose whether or not to **encrypt** your files before hiding them.
* Your files will be encrypted using AES encryption algorithm while the key being your master password.
* Your **Master Password** is encrypted using **PBKDF2** Algorithm with your master password itself as its own key.
* The original files are untouched so you can keep the original file or even delete it after hiding and the choice is completely up to you.
* The vault can be called from anywhere by typing **secret_vault** in the terminal.
* If you wish to unhide a file, then the file will be downloaded in the **current working directory** of the terminal or in simpler terms, the folder from where you called the program.
* You can even delete and reset the whole vault if you wish to after supplying your masterpassword.

## Basic Usage
Here's a simple gif to show you basics of how to use the vault


![](https://i.imgur.com/w0YRsDb.gif)

## Installation
You can install the package using **pip command**
```
pip install secret-vault
```

or by cloning this repo : 
```
git clone https://github.com/Maneesh-Pradeep/secret_vault.git
cd secret_vault

# Run the setup.py file
python setup.py install
```

## Starting vault
You can just type the **secret_vault** command from anywhere in the terminal to start the program.

The first time when you open the program, you are asked to Create a Master Password.
That Master Password is used to identify you and also encrypt your files.

You will be asked to enter your Master Password every time you open the vault.

You can reset the master password by running the **Delete and Reset Vault** command in the program.
