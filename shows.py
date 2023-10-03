from tkinter import *
from tkinter import ttk

import db 

def sss():

	
	show = Tk()
	def calling():
		global cur,con
		call = db.Db()
		cur = call.cur
		cur.execute("")
		con = call.con

	scroll = Scrollbar(show, orient=VERTICAL)
	listbox = Listbox(show,yscrollcommand=scroll.set,height=12)
	listbox.pack(side=LEFT, fill=Y)
	scroll.config (command=listbox.yview)
	scroll.pack(side=RIGHT, fill=Y)
	listbox.config(width=100)
	listbox.pack(side=LEFT,  fill=BOTH, expand=1)



	calling()
	cur.execute("SELECT * FROM user")
	rows = cur.fetchall()
	#for row in rows:
	#	print(row)


	for row in rows:
		c = []
		games = [row[0]]
		for game in games:
			listbox.insert(END, game)
			c.append(game)

	def Selected():
		return int(listbox.curselection()[0])
	def ff():
		#print([Selected()])
		x = Selected()
		global sel1
		global sel2
		sel1 = rows[x][0]
		sel2= rows[x][1]

		#print(sel1)
		#Select_set()
	def buttons(x,y,text,command):
		style = ttk.Style()
		style.configure("My.TButton", padding=10, relief="flat",font=("Helvetica",10,"italic"), foreground="#ce60d6", background="#007BFF")
		button = ttk.Button(show, text=text, style="My.TButton",command=command)
		button.pack()
	b2 = buttons(480,100,"Select !",ff)

	show.mainloop()

