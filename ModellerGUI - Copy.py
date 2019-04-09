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

# Creating mandatory folders
mydir =  datetime.now().strftime("%Y-%m-%d __ [%I-%M-%S-%p]")

# To check the current selected alignment file from /alignments folder
def after_loop_lab1_2(selected_PDB):
   new_text = selected_PDB
   lab1_2 = Label(win,text=new_text, font="Times 16", bg="white",fg='black',cursor='arrow',).grid(row=1 , column=1)
    # modellerF()
    # call again after 500 ms
   # win.after(100, after_loop_lab1_3)
#-----
def after_loop_lab2_2(pdb_name):
   new_text = pdb_name
   lab2_2 = Label(win, text='pdb_95.pir',font="Times 16 ", bg="white" ,anchor='w',padx=100,pady=5, fg='black',relief=SUNKEN).grid(row=3,column=1)

    
#-----
# def changeValue():
#  new_text = random.randint(1,101)
#  lab1_2 = Label(win,text=new_text, font="Times 16 bold", bg="white").grid(row=0, column=1)
#  win.after(500,changeValue)
#-----


def modellerF():
   # Gerenating Logs
   
   log.verbose()
   env = environ()
   function0()
   function1()



   os.makedirs(os.path.join(os.getcwd()+"\\Data\\",mydir))
   os.makedirs(os.path.join(os.getcwd()+"\\Data\\",mydir+"\\Input ALI"))
   os.makedirs(os.path.join(os.getcwd()+"\\Data\\",mydir+"\\Input FASTA"))
   os.makedirs(os.path.join(os.getcwd()+"\\Data\\",mydir+"\\PRF"))
   os.makedirs(os.path.join(os.getcwd()+"\\Data\\",mydir+"\\PDB"))
   os.makedirs(os.path.join(os.getcwd()+"\\Data\\",mydir+"\\Output ALI"))
   os.makedirs(os.path.join(os.getcwd()+"\\Data\\",mydir+"\\PAP"))
   os.makedirs(os.path.join(os.getcwd()+"\\Data\\",mydir+"\\Logs"))
   # Gerenating Logs
   #sys.stdout = open(os.getcwd()+"\\Data\\"+mydir+"\\Logs\\ModellerGUI Log.txt", "w")  # Printing Logs

   # Using Glob Module. Now we can find the files having specific format i.e. .py
   files1 = os.listdir(os.getcwd()+"\\Data\\Alignments")
   for f in files1:
      full_file_name = os.path.join(os.getcwd()+"\\Data\\Alignments", f)
      if (os.path.isfile(full_file_name)):
         shutil.copy(full_file_name, os.getcwd()+"\\Data\\"+mydir+"\\Input ALI")

   list1 =  os.listdir(os.getcwd()+"\\Data\\"+mydir+"\\Input ALI")
   
   # Updating list of alignments to the ListBox
   label2 = Label(win, text="Found Alignment files in folder : ",font="Verdana 16 ",bg="#90A4AE").grid(row=8,column=0)
   listBox1 = Listbox(win,font="Times 16",selectmode=EXTENDED,highlightthickness=5,bg="#90CAF9") #.grid(row=8,column=0)
   count=0
   for x in list1:
      listBox1.insert(count,'['+str(count)+'] '+x)
      count=count+1
   listBox1.grid(row=8,column=1)

   for i in list1:
      selected_PDB = i[:-4]
      
      # This file have all the modeller python file, Which will run one by one.
      # [1] Build_profile.py
      # [2] Compare.py
      # [3] Align2d.py
      # [4] Modelssingle.py
      # [5] Evaluate_model.py
      ###################################################################################################
      #                             Build_Profile.py
      print "# This file have all the modeller python file, Which will run one by one"
      print "#  [1] Build_profile.py"
      print "#  [2] Compare.py"
      print "#  [3] Align2d.py"
      print "#  [4] Modelssingle.py"
      print "#  [5] Evaluate_model.py"
      print "###################################################################################################"
      print "#                                     Build_Profile.py"
      print "###################################################################################################"


      #-- Name of Selected ALI file from \\alignments folder
      print "\n**** Name of  \"Selected_PDB\"    is = "+selected_PDB
      print "\n**** File name is = "+i
      print " "
      
      # Calling this function to update(on runtime) the Current ALI file label in GUI
      after_loop_lab1_2(selected_PDB)
      

      #-- Read in the sequence database
      sdb = sequence_db(env)
      sdb.read(seq_database_file='pdb_95.pir', seq_database_format='PIR',
               chains_list='ALL', minmax_db_seq_len=(30, 4000), clean_sequences=True)
      print "###################################################################################################"
      print "#                                  Build_Profile.py > Sequence,read()"
      print "###################################################################################################"
      
      #-- Write the sequence database in binary form
      sdb.write(seq_database_file='pdb_95.bin', seq_database_format='BINARY', chains_list='ALL')
      print "###################################################################################################"
      print "#                                  Build_Profile.py > Sequence,write()"
      print "###################################################################################################"
      
      #-- Now, read in the binary database
      sdb.read(seq_database_file='pdb_95.bin', seq_database_format='BINARY', chains_list='ALL')
      print "###################################################################################################"
      print "#                                     Build_Profile.py > Sequence,read_Binary()"
      print "###################################################################################################"
      
      # To update PDB Database name on GUI
      after_loop_lab2_2('pdb_95.pir')

      #-- Read in the target sequence\\alignment
      aln = alignment(env)
      aln.append(file=os.getcwd()+"\\Data\\"+mydir+"\\Input ALI\\"+selected_PDB+'.ali', alignment_format='PIR', align_codes='ALL')
      function2()
      print "###################################################################################################"
      print "#                               Build_Profile.py > Appending, writing files in .ali()"
      print "###################################################################################################"
      
      #-- Convert the input sequence\\alignment into
      #   profile format
      prf = aln.to_profile()
      print "###################################################################################################"
      print "#                                Build_Profile.py > Alignment_To_Profile(converstion)"
      print "###################################################################################################"
      
      #-- Scan sequence database to pick up homologous sequences
      prf.build(sdb, matrix_offset=-450, rr_file='${LIB}\\blosum62.sim.mat',
                gap_penalties_1d=(-500, -50), n_prof_iterations=1,
                check_profile=False, max_aln_evalue=0.01)
      print "###################################################################################################"
      print "#                                      Build_Profile.py > Profile.Build()"
      print "###################################################################################################"
      
      #-- Write out the profile in text format
      prf.write(file=os.getcwd()+"\\Data\\"+mydir+"\\PRF\\"+selected_PDB+"_build_profile.prf", profile_format='TEXT')
      print "###################################################################################################"
      print "#                                      Build_Profile.py > Writing, Profile in .prf"
      print "###################################################################################################"
      
      #-- Convert the profile back to alignment format
      aln = prf.to_alignment()
      print "###################################################################################################"
      print "#                                          Build_Profile.py > Profile To Alignment"
      print "###################################################################################################"
      
      #-- Write out the alignment file
      aln.write(file=os.getcwd()+"\\Data\\"+mydir+"\\Output ALI\\"+selected_PDB+"_build_profile.ali", alignment_format='PIR')
      print "###################################################################################################"
      print "#                                         Build_Profile.py > Writing ALignment from Profile"
      print "###################################################################################################"
      
      # Updating the Process status Presenter. It is showing that Profile file has been build successfuly
      
      ###################################################################################################
      #                             Compare.py
      print "###################################################################################################"
      print "#                                      Compare.py"
      print "###################################################################################################"
      
      #env = environ()
      aln = alignment(env)
      # This script will find the best protein based on the below crieterias:
      # [1] LOWEST E-VALUE
      # [2] COVERAGE
      # [3] SEQUENCE LENGTH BASED ON PROCESSING ENZYMES

      # [A] Preparing the data for the Compare.py, and to get the (pdb, chain) from the Build_profile.prf

      # Opening Build_Profile PROFILE file
      file1 = open(os.getcwd()+"\\Data\\"+mydir+"\\PRF\\"+selected_PDB+'_build_profile.prf','r')   
      
      # Updating Process status presentator, showing Optimum PDB file found. AND IT HAVE TO BE REPLACE AFTER THE intvar3 CODE. THIS IS HERE JUST TO CHECK ITS WORKING
      function3()
      # Going through the file 1 line at a time.
      count = 0
      intvar=""
      for i in file1:      
         count = count + 1
         #print("&&&& AM I in For-LOOP ? &&&&")
         if(count > 7):
            #print("&&&& AM I in IF-Condition ? &&&&")
            for j in (i[99:107]):
               if(j != " "):
                  #print("&&&& AM J in IF-Condition ? Fetching Evalue")
                  # fetching the Evalue(string value) of each protein            
                  intvar = intvar+j    
                  
            # Converting a string E-value into Floating point E-Value
            e_value = float(intvar)
            intvar = ""
            
            for j in (i[93:95]):
               if(j != " " and j != "."):
                  #print("&&&& AM J in IF-Condition ? Removing anamoly in data")
                  # Removing any anamoly in the data  
                  intvar = intvar+j    

            # Converting a string Coverage value into Floating point Coverage value
            coverage = float(intvar)      
            intvar = ""

            # fetching the Coverage(percentage value) of each protein 
            for j in (i[87:93]):
               if(j != " " ):
                  #print("&&&& AM J in IF-Condition ? Fetching Coverage")     
                  intvar = intvar+j    

            # Coverting a string Sequence value in to Floating point Sequence value
            seq_len = float(intvar)    
            intvar = ""

            # fetching the PDB name (srting value) of each protein 
            for j in (i[6:12]):
               if(j != " " ):
                  #print("&&&& AM J in IF-Condition ? Fetching PDB name")
                  intvar = intvar+j    

            # Storing the pdb name in to variable        
            pdb_var = intvar
            print "\n\n\n This is the pdb_var: "+pdb_var
            intvar = ""

            # Storing a list of values
            tempList = [e_value,coverage,seq_len,pdb_var]

            # Creating a list of list [e-value, coverage, sequence, pdb]
            intvar3.append(tempList)
            
      # Printing the List of List[3 crietereas]
      print "\n\n\n This is the Profile File: "
      print intvar3
      print "\n\n\n"
      maxE = 0

      # Now Getting the best protein based on the 3 critereas
      for x in intvar3: 
         if x[0] <= maxE:
            maxE = x[3]
            break

      # Allocatin the values to the variables
      print "**** MaxE Name = "+str(maxE)
      pdb = maxE
      chain = 'A'

      # Validatin of the PDB name, whether it is having an extra 'A' at the last of the PDB name or not
      print "**** PDB Name = "+str(pdb)
      if pdb[-1] == 'A':
         pdb = pdb[:-1]
      print "**** PDb, Chains are: "+pdb+chain
      
      
      # Downloading selected PDB file from Wget, Runtime
      url = "https://files.rcsb.org/download/"+pdb+".pdb"  # Actual Code, The following one will not be valid code.
      # url = "https://files.rcsb.org/download/1bdm.pdb" # Just for Try
      file1 = wget.download(url, os.getcwd()+"\\Data\\"+mydir+"\\PDB\\")

      # [B] Actual Compare.py starts here
      #     All codes above were for the preparing the data only
      #    Now we have best (pdb, chain)
      m = model(env, file=os.getcwd()+"\\Data\\"+mydir+"\\PDB\\"+pdb+".pdb", model_segment=('FIRST:'+chain, 'LAST:'+chain))
      print "**** Model is Made"
      aln.append_model(m, atom_files=os.getcwd()+"\\Data\\"+mydir+"\\PDB\\"+pdb,  align_codes=pdb+chain)
      aln.malign()
      aln.malign()
      aln.malign3d()
      aln.compare_structures()
      aln.id_table(matrix_file='family.mat')


      ###################################################################################################
      #                             Align2D.py
      print("###################################################################################################")
      print("#                                        Align2D.py")
      print("###################################################################################################")
      # Align2D starts from here

      
      #import Compare as tryPy1
      #env = environ()
      aln = alignment(env)
      #mdl = model(env, file=pdb, model_segment=('FIRST:A','LAST:A'))
      mdl = model(env, file=os.getcwd()+"\\Data\\"+mydir+"\\PDB\\"+pdb, model_segment=('FIRST:A','LAST:A'))
      aln.append_model(mdl, align_codes=pdb+chain, atom_files=os.getcwd()+"\\Data\\"+mydir+"\\PDB\\"+pdb+'.pdb')  
      aln.append(file=os.getcwd()+"\\Data\\"+mydir+"\\Output ALI\\"+selected_PDB+'_build_profile.ali', align_codes=selected_PDB)
      aln.align2d()
      aln.write(file=os.getcwd()+"\\Data\\"+mydir+"\\Output ALI\\"+selected_PDB+'-'+pdb+chain+'.ali', alignment_format='PIR')
      aln.write(file=os.getcwd()+"\\Data\\"+mydir+"\\PAP\\"+selected_PDB+'-'+pdb+chain+'.pap', alignment_format='PAP')


      ###################################################################################################
      #                             Model-Single.py
      print("###################################################################################################")
      print("#                                              Model-Single.py")
      print("###################################################################################################")

      a = automodel(env, alnfile=os.getcwd()+"\\Data\\"+mydir+"\\Output ALI\\"+selected_PDB+'-'+pdb+chain+'.ali',
                    knowns=pdb+chain, sequence=selected_PDB,
                    assess_methods=(assess.DOPE,
                                    #soap_protein_od.Scorer(),
                                    assess.GA341))
      a.starting_model = 1
      a.ending_model = 5
      a.make()

      # Updating the Process status Presenter. It will tell us that the Model is created for the current ALI file
      function4()
      ###################################################################################################
      #                             Evaluate_Model.py
      print("###################################################################################################")
      print("#                                              Evaluate_Model.py")
      print("###################################################################################################")

      #log.verbose()    # request verbose output
      #env = environ()
      env.libs.topology.read(file='$(LIB)\\top_heav.lib') # read topology
      env.libs.parameters.read(file='$(LIB)\\par.lib') # read parameters

      # read model file
      mdl = complete_pdb(env, selected_PDB+'.B99990002.pdb')

      # Assess with DOPE:
      s = selection(mdl)   # all atom selection
      s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file=selected_PDB+'.profile',
                    normalize_profile=True, smoothing_window=15)

#----------    
def modellerFCall():
   b1 = Button(win,text="Runninng..",cursor='watch', font="Helvetica 14",anchor='w',padx=80,pady=20,relief=SUNKEN,activebackground='lightgrey',activeforeground="blue",fg="#90A4AE").grid(row=8,column=3)
   modellerF()
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

def modellerGUI():
   win = Tk()

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

#---------

if __name__ == '__main__':   

   