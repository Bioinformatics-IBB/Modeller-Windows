import os
selected = "B0FGV7"
dash = "-"
pdb = "5a2g"
chain = "A"

file = open(os.getcwd()+"\\"+selected+dash+pdb+chain+".ali","r")
fileTemp = open(os.getcwd()+"\\"+selected+dash+pdb+chain+".ali.tmp","w+")
#import selectedpdbchain
#print(file.read())


i = 0
k=0


for x in file:
	i=i+1 # Line count

	if i == 3:
		k=0
		singleLine = x[0:11]
		print("Printing singleLine in IF: ",singleLine)
		for j in x:
			#print("Value of Kkkkkkk: ",k)
			k = k+1 # index count
			if x[k] == "P" and x[k+1] == "D" and x[k+2] == "B" and x[k+3] == "\\":
				print("::IF statement IS working::")
				singleLine = singleLine+x[k+4:]
				print("Printing singleLineeeeeeeeeee: ", singleLine)
				fileTemp.write(singleLine)
				break
			print("::IF statement not working::")
			
		
			
		#print("Printing singleLineeeeeeeeeee: ", singleLine)
	else:
		#k = k+1 # index count
		singleLine = x
		#print("Printing singleLine in ELSE: ",singleLine)
		print(singleLine)
		fileTemp.write(singleLine)

file.close()
fileTemp.close()

os.remove(selected+dash+pdb+chain+".ali")
os.rename(selected+dash+pdb+chain+".ali.tmp",selected+dash+pdb+chain+".ali")
