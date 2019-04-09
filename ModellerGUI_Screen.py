import threading
import tkFileDialog, shutil # For Copying file from one folder to another
from datetime import datetime 
from Tkinter import *
import os
import random
from Tkinter import *
from modeller import *
from modeller.automodel import *
from modeller.scripts import complete_pdb
import glob,os
import wget
import sys
import ModellerGUI_Controller as MdC

selected_PDB=" "
maxE = 0.0
count = 0
intvar =""
pdb_var = ""
pdb=""
chain = ""  
intvar2 = 0.0
intvar3 = []
evalueList = []
e_value = 0.0
coverage=0.0
seq_len=0
i=""
j=""
new_text =""
list1=""
count=0
win = Tk()
# Creating mandatory folders
mydir =  datetime.now().strftime("%Y-%m-%d __ [%I-%M-%S-%p]")

# To check the current selected alignment file from /alignments folder
def after_loop_lab1_2(selected_PDB):
   new_text = selected_PDB
   lab1_2 = Label(win,text=new_text, font="Times 16", bg="white",fg='black',cursor='arrow').grid(row=1 , column=1)
    # modellerF()
    # call again after 500 ms
   # win.after(100, after_loop_lab1_3)
#-----
def after_loop_lab2_2(pdb_name):
   new_text = pdb_name
   lab2_2 = Label(win, text='pdb_95.pir',font="Times 16 ", bg="white" ,anchor='w',padx=100,pady=5, fg='black',relief=SUNKEN).grid(row=3,column=1)

    
#-----
# def changeValue():
# 	new_text = random.randint(1,101)
# 	lab1_2 = Label(win,text=new_text, font="Times 16 bold", bg="white").grid(row=0, column=1)
# 	win.after(500,changeValue)
#-----


#----------    
def modellerFCall():
   b1 = Button(win,text="Runninng..",cursor='watch', font="Helvetica 14",anchor='w',padx=80,pady=20,relief=SUNKEN,activebackground='lightgrey',activeforeground="blue",fg="#90A4AE").grid(row=8,column=3)
   ModellerThread =  threading.Thread(target=MdC.modellerF())
   ModellerThread.start()
#----------

#----------
def fastaFileOpener():
   filez = tkFileDialog.askopenfilenames(parent=win,title='Choose a file')
   for x in filez:
      print x
      shutil.copy(x,os.getcwd()+"\\Data\\FASTA\\")

#----------
def aliFileOpener():
   filez = tkFileDialog.askopenfilenames(parent=win,title='Choose a file')
   for x in filez:
      print x
      shutil.copy(x,os.getcwd()+"\\Data\\Input ALI\\")
#----------
#----------
def function0():
   processOne = Label(win, text="Environment Created",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="white").grid(row=11,column=0)
   processTwo = Label(win, text="Profile File Build",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="white").grid(row=11,column=1)
   ProcessThree = Label(win, text="Optimum PDB Found",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="white").grid(row=11,column=2)
   ProcessFour = Label(win, text="Model Created",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="white").grid(row=11,column=3)
   
#----------   
def function1():
   lab1 = Label(win, text="Environment Created",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="#90CAF9").grid(row=11,column=0)
   
#----------   
def function2():
   lab2 = Label(win, text="Profile File Build",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="#90CAF9").grid(row=11,column=1)
   
#----------   
def function3():
   lab3 = Label(win, text="Optimum PDB Found",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="#90CAF9").grid(row=11,column=2)
   
#----------   
def function4():
   lab4 = Label(win, text="Model Created",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="#90CAF9").grid(row=11,column=3)
   
#----------  

def GUIBuilder():

   
   #Declaring Text
   lab1Text = Label(win, text="Open files",font="Verdana 16 bold" ,anchor='w',padx=100,pady=5, fg='black',bg='#90A4AE').grid(row=0, column=0)
   b1 = Button(win, text="Open FASTA Files", font="Helvetica 14", command=fastaFileOpener,anchor='w',padx=10,pady=10,relief=GROOVE,bg='#80CBC4',activebackground='lightgrey',activeforeground="blue").grid(row=0,column=1) #,command=
   b1 = Button(win, text="Open ALI Files", font="Helvetica 14", command=aliFileOpener,anchor='w',padx=25,pady=10,relief=GROOVE,bg='#80CBC4',activebackground='lightgrey',activeforeground="blue").grid(row=0,column=2) #,command=

   # Label: Current Alignment File
   lab1 = Label(win, text='Current Alignment File',font="Verdana 16 " ,anchor='w',padx=100,pady=5, fg='black',bg="#90A4AE" ).grid(row=1)
   lab1_2 = Label(win,text='Loading..', font="Times 16 ",padx=100,pady=5,bg='white',fg='black',anchor='w',relief=SUNKEN,cursor='arrow').grid(row=1, column=1)
   # updatedText.set(after_loop())
   # changeValue()
   # after_loop_lab1_2()

   # label : PDB Database
   lab2 = Label(win, text='PDB Database',font="Verdana 16",anchor='w',padx=100,pady=5, fg='black',bg="#90A4AE").grid(row=3)
   lab2_2 = Label(win, text='Loading..',font="Times 16 ", bg="white" ,anchor='w',padx=100,pady=5, fg='black',relief=SUNKEN).grid(row=3,column=1)

   # Label : PDB from Profile-file
   lab3 = Label(win, text='PDB from Profile-File',font="Verdana 16",anchor='w',padx=100,pady=5, fg='black',bg="#90A4AE").grid(row=4)
   lab3_3 = Label(win, text='Loading..',font="Times 16 ", bg="white" ,anchor='w',padx=100,pady=5, fg='black',relief=SUNKEN).grid(row=4,column=1)

   # label : Complete-PDB
   lab4 = Label(win, text='Complete-PDB',font="Verdana 16",anchor='w',padx=100,pady=5, fg='black',bg="#90A4AE").grid(row=5)
   lab4_4 = Label(win, text='Loading..',font="Times 16", bg="white" ,anchor='w',padx=100,pady=5, fg='black',relief=SUNKEN).grid(row=5,column=1)

   # This one is for making a better Identation in GUI (Jugaad)
   extraLabel12 = Label(win, bg="#90A4AE").grid(row=6)

   # This is to show the List of all alignment files in the source /alignment folder
   label2 = Label(win, text="Found Alignment files in folder : ",font="Verdana 16",bg="#90A4AE").grid(row=8,column=0)
   listBox1 = Listbox(win,font="Times 16",selectmode=EXTENDED,highlightthickness=5).grid(row=8,column=1)
      
   # Button to start the Modeller
   # ThreadmodellerFCall= modellerFCall()
   b1 = Button(win, text="Start", font="Helvetica 14", command=modellerFCall,anchor='w',padx=100,pady=20,relief=GROOVE,bg='#80CBC4',activebackground='lightgrey',activeforeground="blue").grid(row=8,column=3) #,command=modellerF

   # Button to quit
   b2 = Button(win, text='Quit', font="Helvetica 14", command=win.quit,anchor='w',padx=100,pady=20,activebackground='lightgrey',bg="#80CBC4",activeforeground="red",relief=GROOVE).grid(row=13,column=3)
   
   # This one is for making a better Identation in GUI (Jugaad)
   extraLabel1 = Label(win,bg="#90A4AE").grid(row=10)

   # Process Status presenter
   processOne = Label(win, text="Environment Created",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="white").grid(row=11,column=0)
   processTwo = Label(win, text="Profile File Build",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="white").grid(row=11,column=1)
   ProcessThree = Label(win, text="Optimum PDB Found",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="white").grid(row=11,column=2)
   ProcessFour = Label(win, text="Model Created",font="Verdana 16",anchor='w',padx=10,pady=10,relief=GROOVE, fg='black',bg="white").grid(row=11,column=3)

   # This one is for making a better Identation in GUI (Jugaad)
   extraLabel1 = Label(win,bg="#90A4AE").grid(row=12)

   #GUI configurations
   win.geometry("1400x700")
   win.configure(bg="#90A4AE")
   win.mainloop() 
if __name__ == '__main__':   

   GUIThread = threading.Thread(target=GUIBuilder())
   GUIThread.start()
   