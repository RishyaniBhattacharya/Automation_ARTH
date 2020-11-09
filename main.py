#!/usr/bin/python3
import os

def logo():
	print("""\033[33m
	
██████╗ ██╗   ██╗███╗   ██╗ █████╗ ███╗   ███╗██╗ ██████╗███████╗
██╔══██╗╚██╗ ██╔╝████╗  ██║██╔══██╗████╗ ████║██║██╔════╝██╔════╝
██║  ██║ ╚████╔╝ ██╔██╗ ██║███████║██╔████╔██║██║██║     ███████╗
██║  ██║  ╚██╔╝  ██║╚██╗██║██╔══██║██║╚██╔╝██║██║██║     ╚════██║
██████╔╝   ██║   ██║ ╚████║██║  ██║██║ ╚═╝ ██║██║╚██████╗███████║
╚═════╝    ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝ ╚═════╝╚══════╝
																
\033[32m        A Menu Driven Python Automation Tool.
\033[34m                     :Authors:
\033[34m[✔] Rishyani Bhattacharya (https://www.linkedin.com/in/rishyani-bhattacharya-6414b8194/)
\033[34m[✔] Dipaditya Das         (https://www.linkedin.com/in/dipadityadas/)
\033[34m[✔] Alok Raj              (https://www.linkedin.com/in/alok-rithvik/)
\033[34m[✔] Niket Ranjan          (https://www.linkedin.com/in/niket24/)
\033[34m[✔] Abhishek Anand        (https://www.linkedin.com/in/abhishek-anand-88576a1a4/)
\033[97m """)

def color(c):
	os.system('tput setaf {}'.format(c))

def clear():
    os.system('clear')

def main():
	logo()
	input("Press any key to continue....")
	while True:
		clear()
		color(7)
		

main()