from Tkinter import *
import threading
import "ModellerGUI - Controller"

def main():
	root = Tk()
	lab1 = Label(root, text="Haha ",bg="#292D3E",font="Helvetica 12",fg="#FDF4DF").pack()

	root.geometry("400x400")
	root.configure(bg="#292D3E")

	root.mainloop()


if __name__ == '__main__':
	ThreadMain = threading.Thread(target=main())
	ThreadMain.start()