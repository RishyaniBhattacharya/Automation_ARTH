#!/usr/bin/python3
import os
from platform import system

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
	color(6)
	input("Press any key to continue....")

	while True:
		clear()
		color(7)
		print('\n\t\t\t    Main Menu')
		print('\t\t==================================\n')
		color()
		menu = ['Linux', 'Docker', 'Hadoop', 'AWS']
		for i in range(len(menu)):
			print('\t\t\tEnter {} : {}'.format(i+1, menu[i]))
		color(2)
		print('\t\t\tEnter 0 : Go Back')
		color(1)
		print('\t\t\tEnter e : To Exit')
		color(5)
		choice = input('Enter your choice : ')
		if choice == '0':
			from loc_rem import local_remote
			local_remote()
		elif choice == '1':
			from linux import linux_func
			linux_func(arg, ip)
		elif choice == '2':
			from docker import docker_menu
			docker_menu(arg, ip)
		elif choice == '3':
			from hadoop import hadoop_func
			hadoop_func(arg, ip)
		elif choice == '4':
			from aws import aws_func
			aws_func(arg, ip)
		elif choice == 'e':
			clear()
			color(7)
			exit()
		else:
			print('Invalid choice !')

main()
