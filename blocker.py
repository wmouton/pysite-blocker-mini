from tkinter import *
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Website Blocker")
Label(root, text='Website Blocker', font='arial 20 bold').pack()
host_path = `C:\Windows\System32\drivers\etc\hosts`
ip_address = '127.0.0.1'
Label(root, text = 'Enter Website : ', font = 'arial 13 bold').places(x=5, y=60)
Websites = Text(root, font = 'arial 10', height = '2', width = '40')
Websites.place(x = 140, y = 60)


def Blocker():
	website_lists = Websites.get(1.0,END)
	Website = list(website_lists.split(","))
	