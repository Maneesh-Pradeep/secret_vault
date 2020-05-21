# Secret Vault
A secret file storage vault in python for MacOS and Linux systems.

# Features
* Store and encrypt your files in an hidden directory somewhere in your PC.
* The freedom to choose whether or not to **encrypt** your files before hiding them.
* Your files will be encrypted using AES encryption algorithm while the key being your master password.
* Your **Master Password** is encrypted using **PBKDF2** Algorithm with your master password itself as its own key.
* The original files are untouched so you can keep the original file or even delete it after hiding and the choice is completely up to you.
* The vault can be called from anywhere by typing **secret_vault** in the terminal.
* If you wish to unhide a file, then the file will be downloaded in the **current working directory** of the terminal or in simpler terms, the folder from where you called the function.
* You can even delete and reset the whole vault if you wish to after supplying your masterpassword.

