import os
import sys, time
import sys,time
import getpass
def spin():
    try:
        L="/-\\|"
        for q in range (100):
            time.sleep(0.1)
            sys.stdout.write("\r["+L[q % len(L)]+"]")
            sys.stdout.flush()
    except:
            exit()

def ketik(text):
    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)


# Aplikasi untuk management password

os.system("cls")

print('\33[92m' + "============SELAMAT DATANG==============")
apk = input("Masukkan nama aplikasi \t:")
username = input("Masukkan username atau Email anda \t:")
password = getpass.getpass("Masukkan Password \t:")
spin()
ketik(
    '===========================\n'
    '\33[91m'+
    "===========================\n"
    "PASSWORD BERHASIL DISIMPAN\n"
    "============================\n"
    +'\033[0m'
)


# ini adalah format teks yang akan ditampilkan pada file txt
teks ="""
======================
Nama Aplikasi  \t:{}
Username/Email \t:{}
Password       \t:{}
""".format(apk,username,password)

# buka file
filepas = open("pass.txt", "a")
filepas.write(teks)
filepas.close()

