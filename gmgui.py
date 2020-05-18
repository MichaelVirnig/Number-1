#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  gmgui.py - I wrote this to be a helper app that runs at startup and gives 
#  gui access to tasks I run when I first log in or startup kali linux
#
#  Copyright 2020 <mediocre mike>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import tkinter as tk
from tkinter.filedialog import askopenfile, askopenfilename
from tkinter import StringVar, IntVar
import subprocess, time, sys, os, requests, webbrowser, random

##build window
window = tk.Tk()
window.configure(bg='light blue') ## background color for the window

##build textbox with scrollbar
frame1 = tk.Frame(window,width=80, height=80,bg = '#ffffff',borderwidth=1, relief="sunken")
scrollbar = tk.Scrollbar(frame1) 
editArea = tk.Text(frame1, width=70, height=38, wrap="word",yscrollcommand=scrollbar.set,borderwidth=5, 
					highlightthickness=0, font=("Hack 7"),padx = 10, pady = 10)
scrollbar.config(command=editArea.yview)
scrollbar.pack(side="right", fill="y")
editArea.pack(side="left", fill="both", expand=True)
frame1.grid(rowspan=11,column=1,padx = 10, pady = 10)

## set labels for vpn text displays
vpn_txt=StringVar()
vpn_txt.set("VPN OFF")
vpn_txt1=StringVar()
vpn_txt1.set("HTB IP: ")

#entry box
entry1 = tk.Entry(window, bd=4, width=38)
entry1.grid(row=11, column=1)

#####	FUNCTIONS	#####

## good morning ascii
def good_morning():
	#cowsay character options, default selection on kali 
	list1=("apt","bud-frogs","bunny","calvin","cheese","cock","cower","daemon","default","dragon","dragon-and-cow","duck","elephant",
	"elephant-in-snake","eyes","flaming-sheep","fox","ghostbusters","gnu","hellokitty","kangaroo","kiss","koala","kosh","luke-koala",
	"mech-and-cow","milk","moofasa","moose","pony","pony-smaller","ren","sheep","skeleton","snowman","stegosaurus","stimpy","suse",
	"three-eyes","turkey","turtle","tux","unipony","unipony-smaller","vader","vader-koala","www")
	#cowsay quotes
	list2=("Regret Nothing!!","Do More, Try Something Different!!!","Lets Do This!!","Carpe Diem!","Try Harder!!","Hack all the Things!!!",
	"Slow if Fast and Fast is Smooth!","Git Gud!","Git Guder!","LEEEEERROOOOYYYYY JENNNNKKIINNNNSSSS","Enum Enum Enum","Check Your Syntax",
	"Check Your Notes!","Dont Give Up, Double Check Your Code!","Save Your work!","Record Your Progress")
	x=random.choice(list1) # select a random character from list1
	y=random.choice(list2) # select a random quote from list2
	cmd2=("/usr/games/cowsay -f "+x+" "+y) # cowsay command with the random items from list1 and list2
	o=subprocess.Popen(cmd2,stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True, text=True, universal_newlines=True)
	while True:# this while loop prints line by line in order
		line = o.stdout.readline()
		if not line:
			break
		editArea.insert('end',line)
		editArea.see('end')
		editArea.update_idletasks()
	
##get command from entry1, run the command and print output line by line
def get_cmd():
	x1 = entry1.get()
	entry1.delete(0,'end')
	if x1 == 'clear':
		clearall()
	else:
		x2=subprocess.Popen(x1,stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True, text=True, universal_newlines=True)
		while True:
			line = x2.stdout.readline()
			if not line:
				break
			editArea.insert('end', line)
			editArea.see('end')
			editArea.update_idletasks()

## apt-get update && apt-get upgrade
def updatesys():
	cmd = ("apt-get update && apt-get upgrade -y")
	o=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True, text=True, universal_newlines=True)
	while True:
		line = o.stdout.readline()
		if not line:
			break
		editArea.insert('end',line)
		editArea.see('end')
		editArea.update_idletasks()
		
## Mount shared folder function, used absolute path to my mount-shared-folders scripts
def mountshare():
	p=subprocess.Popen("/root/mount-shared-folders",stdout=subprocess.PIPE,stderr=subprocess.PIPE, 
						universal_newlines=True)
	output, errors = p.communicate()
	editArea.insert('end', output)
	
## launch cherrytree
def ctree():
	cmd = ("/usr/bin/cherrytree")
	c=subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True,text=True)

## launch terminator, replace cmd var to launch different terminal
def open_term():
	cmd=("/usr/bin/terminator")
	t=subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True,text=True)
	
## launch chrome browser, replace chrome_path if using different browser
def web():
	chrome_path = '/usr/bin/google-chrome-stable %U'
	d = subprocess.Popen(chrome_path, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True,text=True)
	
## start htb vpn, using absolute path to my htb vpn config file
def startvpn():
	openvpn_cmd = ("/usr/sbin/openvpn --config /root/lab-connection/mediocre.ovpn")
	q=subprocess.Popen(openvpn_cmd, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, 
	shell=True,text=True, universal_newlines=True)
	editArea.insert('end',"			<<<<<VPN Launched!>>>>>"+"\n\n")
	editArea.insert('end',"Don't forget to close the VPN when finished by clicking Kill VPN button"+"\n\n")
	
## get ip to verify vpn is running
def getip():
	getipcmd = ("ip -4 addr show tun0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'") ##display only the ipadress
	time.sleep(6)
	r = subprocess.Popen(getipcmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True, text=True)
	output, errors = r.communicate()
	if len(output)<16:
		vpn_txt1.set("IP: "+output.rstrip())# rstrip used to remove trailing \n from output
	else:
		vpn_txt1.set("HTB IP: ")
		vpn_txt.set("VPN OFF")
		
#change vpn txt to reflect running vpn
def lbl_change():
	vpn_txt.set("<<VPN ON>>")

## clear text box	
def clearall():
	editArea.delete("1.0","end")
	
## kill vpn and exit gui
def quitall():
	time.sleep(.5)
	killcmd = ("/usr/bin/killall openvpn")
	os.system(killcmd)
	window.quit()
	
# stop vpn, probably a better way to do this
def quitvpn():
	time.sleep(.5)
	killcmd = ("/usr/bin/killall openvpn")
	os.system(killcmd)
	editArea.insert('end',"			<<<<<VPN Stopped!>>>>>")
	
## open file manager
def open_file(): 
	filename = askopenfilename(initialdir="/root",title="Select file",filetypes=(('Python Files', '*.py'),("all files", "*.*")))
	if filename: 
		cmd=("geany "+filename)#I use geany, replace with your text editor of choice
		os.system(cmd) 
	elif filename == "":
		pass

	
def main():
	#####	BUTTONS	#####
	#button for update/upgrade
	update_button = tk.Button(window, text="Update System", fg='blue', background='light grey', activeforeground="white", 
	activebackground="green", width=15, command=updatesys).grid(row=0, padx = 20, pady = 10)

	#button to mount shared folders
	mount_button = tk.Button(window, text="Mount OSCP Folder", fg='blue', background='light grey', activeforeground="white", 
	activebackground="green", width=15, command=mountshare).grid(row=1, padx = 20, pady = 10)

	#button for cherrytree
	ct_button = tk.Button(window, text="Open Cherrytree", fg='blue', background='light grey', activeforeground="white", 
	activebackground="green", width=15, command=ctree).grid(row=2, padx = 20, pady = 10)
	
	#open terminator
	term_button=tk.Button(window, text="Open Terminator", fg='blue', background='light grey', activeforeground="white", 
	activebackground="green", width=15, command=open_term).grid(row=3, padx = 20, pady = 10)

	#button for browser
	web_button = tk.Button(window, text="Open Chrome", fg='blue', background='light grey', activeforeground="white", 
	activebackground="green", width=15, command=web).grid(row=4, padx = 20, pady = 10)	
			
	#button for vpn
	vpn_button = tk.Button(window, text="Launch HTB vpn", fg='blue', background='light grey', activeforeground="white", 
	activebackground="green", width=15, command=lambda:[startvpn(),getip(),lbl_change()]).grid(row=5, padx = 20, pady = 10)
	
	#label for vpn
	vpn_lbl = tk.Label(window, textvariable=vpn_txt,fg="white", bg='light blue', font="hack 8").grid(row=6)
	vpn_lbl1 = tk.Label(window, textvariable=vpn_txt1,fg="white",bg='light blue', font="hack 8").grid(row=7)
	
	# file manager button
	file_btn = tk.Button(window, text="Open File Manager",fg='blue', background='light grey', activeforeground="white", 
	activebackground="green", width=15, command=lambda:open_file()).grid(row=8, padx = 20, pady = 10)

	#button to clear text box
	clear_button = tk.Button(window, text="Clear", fg='blue', background='light grey', activeforeground="white", 
	activebackground="green", width=15, command=clearall).grid(row=9, padx = 20, pady = 10)
	
	#button to quit vpn
	quit_button = tk.Button(window, text="Kill VPN", fg='white', background='orange', activeforeground="red", 
	activebackground="grey", width=15, command=lambda:[quitvpn(),getip()]).grid(row=10, padx = 20, pady = 10)
	
	#button to quit program and kill services
	quit_button = tk.Button(window, text="Quit/Kill VPN", fg='white', background='orange', activeforeground="red", 
	activebackground="grey", width=15, command=quitall).grid(row=11, padx = 20, pady = 10)
	
	# command entry button
	enter_button = tk.Button(window, text="Enter", fg="white", background="grey", activeforeground="white", 
	activebackground="green",width=10, command=lambda:get_cmd()).grid(row=11, column=1, sticky="E",padx = 10, pady = 10)
	window.bind('<Return>',lambda event: get_cmd())
	
	# motivation button
	motivation_btn = tk.Button(window, text="?", fg="orange", background="blue", activeforeground="blue", 
	activebackground="green",width=3, command=good_morning).grid(row=11, column=1, sticky="W",padx = 14, pady = 0)

if __name__ == "__main__":
    main()
    
good_morning()#get a good morning character and quote on startup

window.title("GOOD MORNING")
window.geometry("710x570+10+10")
window.mainloop()
