from tkinter import *
from tkinter import ttk
import db 
root = Tk()
root.geometry("600x600")
root.configure(bg="#fff")
root.title("save")
data = []


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
		e1.insert(END,sel1)
		e2.insert(END,sel2)


		#print(sel1)
		#Select_set()

	def buttons(x,y,text,command):
		style = ttk.Style()
		style.configure("My.TButton", padding=10, relief="flat",font=("Helvetica",10,"italic"), foreground="#ce60d6", background="#007BFF")
		button = ttk.Button(show, text=text, style="My.TButton",command=command)
		button.pack()
	b2 = buttons(480,100,"Select !",ff)

	show.mainloop()
def calling():
	global cur,con
	call = db.Db()
	cur = call.cur
	cur.execute("")
	con = call.con
	#cur.execute("DELETE FROM user")
def query():
	cur.execute()


def buttons(x,y,text,command):
	style = ttk.Style()
	style.configure("My.TButton", padding=10, relief="flat",font=("Helvetica",10,"italic"), foreground="#ce60d6", background="#007BFF")
	button = ttk.Button(root, text=text, style="My.TButton",command=command)
	button.place(x=x,y=y)
def save():
	se1 = e1.get()
	se2 = e2.get()
	cur.execute("INSERT INTO user(name,data) VALUES (?,?)",(se1,se2))
	cur.execute("SELECT * FROM user")
	con.commit()


def show():

	
	sss()

	
	#e1.set(shows.sel1)
	cur.execute("SELECT * FROM user")
	rows = cur.fetchall()
	for row in rows:
		print(row)

	
def delet():
	
	cur.execute("DELETE FROM `user` WHERE `name` IN (%s, %s)", (sel1, sel2))


def clearing():
	#print(help(con))
	con.cursor()
	
	#calling()
	cur.execute("DELETE FROM user")
	#file_data = open('data.txt','w')
	con.commit()

	
font=("Helvetica",19,"italic")
l1 = Label(root , text="simple app for save your data",font=(font),bg="#fff",fg="#b77c7c")
l1.pack(fill=X)
l1 = Label(root , text="enter your name :",font=(font),bg="#fff",fg="#68c2d8")
l1.pack(fill=X)


e1 = Entry(root,font=(font),justify="center")
e1.place(x=155,y=99)

l2 = Label(root , text="enter your data :",font=(font),bg="#fff",fg="#68c2d8")
l2.place(x=205,y=170)
e2 = Entry(root,font=(font),justify="center")
e2.place(x=155,y=240)
b1 = buttons(480,100,"save !",save)
b2 = buttons(480,180,"show !",show)
b3 = buttons(480,260,"edit !",lambda: None)
b4 = buttons(480,340,"clear all data !",clearing)
b5 = buttons(480,420,"delet !",delet)

calling()

root.mainloop()
"""
#b1 = Button(root,text="save !")
#b1.place(x=500,y=150)
	data.clear()
	data.append([se1,se2])
	file_data = open('data.txt','a')
	file_data.write("{}".format(data))
"""