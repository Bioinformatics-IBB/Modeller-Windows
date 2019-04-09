from Tkinter import *
import threading
import ModellerGUI_Controller as MGC

def main():
	root = Tk()
	frame1 = Frame(root)
	lab1 = Label(root, text="Hehe",bg="#292D3E",font="Helvetica 12",fg="#FDF4DF").pack()
	scrollbar = Scrollbar(frame1)
	scrollbar.pack(side=RIGHT, fill=Y)
	listBox1 = Listbox(frame1,font="Helvetica 12",selectmode=EXTENDED,highlightthickness=0,relief="solid",bg="#2f343f",fg="#FDF4DF",yscrollcommand = Scrollbar.set)
    # scrollbar.pack( side = RIGHT, fill = Y )
	count=1
	list1 = MGC.haha

	for x in list1 :
		listBox1.insert(count,' ['+str(count)+']  '+x)
		count=count+1

	listBox1.pack()	
	scrollbar.config(command=listBox1.yview)
	frame1.pack()
	root.geometry("400x400")
	root.configure(bg="#292D3E")

	root.mainloop()


if __name__ == '__main__':
	ThreadMain = main()
	ThreadMain.start()