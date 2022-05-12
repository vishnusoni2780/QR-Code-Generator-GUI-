import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkm
from PIL import ImageTk, Image
import qrcode,os
import time
import tkinter.messagebox as tkm

win=tk.Tk()
win.geometry('1536x864')
win.title("QR Code Generator")
win.configure(background="Black")

# LOGO
image = Image.open("c:/Users/vishnu/OneDrive/Documents/python/qr_gen/banner.png")
resize_image = image.resize((800, 225))
img = ImageTk.PhotoImage(resize_image)
label1 = tk.Label(win,image=img).pack()

# LINK PORTION
label2=tk.Label(win, text="Enter Link :",fg="white",bg='gray6')
label2.place(x=606 , y=375)
link = StringVar()
entry_field_link = Entry(win,textvariable = link, width ='50')
entry_field_link.place(x=685 , y=375)
#link=entry_field_link.get()

# QR IMG NAME PORTION
label3=tk.Label(win, text="Enter QR-Name : ",fg="white",bg='gray6')
label3.place(x=575 , y=450)
imgs = StringVar()
entry_field_imgs = Entry(win,textvariable = imgs, width ='50')
entry_field_imgs.place(x=685 , y=450)
#imgs=entry_field_imgs.get()

# FUNCTIONS
def bahr():
	exit()
def qrz():
	def close():
		win2.destroy()

	win2=tk.Toplevel()
	win2.geometry('500x500')
	win2.title("Your QR Code")
	win2.configure(background="Black")

	link=entry_field_link.get()
	imgs=entry_field_imgs.get()

	if link=='' and imgs=='':
		tkm.showinfo("MISSING","BLANK ERROR.")
		win2.destroy()
	
	elif link=='' or imgs=='':
		tkm.showinfo("MISSING","One field is missing.")
		win2.destroy()

	else:
		qrimg = qrcode.make("{}".format(link))
		qrimg.save("{}.jpg".format(imgs))
		
# to be work
	def rmvf():
		os.remove("{}.jpg".format(imgs))
		tkm.showinfo("Removing...","Image removed successfully!")
		win2.destroy()

	w2l=tk.Label(win2, text="I've Saved it for you, You can check your storage folder.",font=("Chiller",19,'bold'),fg="white",bg='gray6').place(x=10,y=10)
	w2l=tk.Label(win2, text="SCAN here 👇",font=("Algerian",30,'bold'),fg="white",bg="gray6").place(x=125,y=60)

	p2img= Image.open("c:/Users/vishnu/OneDrive/Documents/python/qr_gen/{}.jpg".format(imgs))
	resize_imgp2 = p2img.resize((250,250))
	imgp2 = ImageTk.PhotoImage(resize_imgp2)
	iconp2 = tk.Label(win2,image=imgp2)
	iconp2.place(x=125,y=125)

	rmvb=tk.Button(win2, text="Remove",width=10,height=2,fg='white',bg='gray20',command=rmvf).place(x=150,y=400)
	button2=tk.Button(win2, text="Exit",width=10,height=2,fg='white',bg='gray20',command=close).place(x=275,y=400)
	win2.mainloop()

# BOTTOM
button1=tk.Button(win, text="Submit",width=10,height=2,fg='white',bg='gray20', command=qrz)
button1.place(x=700 , y=600)
button2=tk.Button(win, text="Exit",width=10,height=2,fg='white',bg='gray20',command=bahr)
button2.place(x=800 , y=600)

label=tk.Label(win, text="© Copyright 2021 : @VishnuSoniDhupad",fg="white",bg='gray6').pack(side='bottom')
win.mainloop()