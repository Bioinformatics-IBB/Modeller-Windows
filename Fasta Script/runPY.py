from Tkinter import *
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import os
import shutil
def fastaFileSelector():
	filename=""
	filename = tkFileDialog.askopenfilename(parent=root,title = "Select FASTA file",filetypes = [("FASTA Files","*.fasta")],multiple=1)
	# files1 = os.listdir(os.getcwd()+"\\alignments")
	for f in filename:
		full_file_name = f
		if (os.path.isfile(full_file_name)):
			shutil.copy(full_file_name, os.getcwd()+"\\fasta2")
root = Tk()
button1 = Button(root, text="Select FASTA Files", command=fastaFileSelector).pack()
root.geometry("200x200")
root.mainloop()
	