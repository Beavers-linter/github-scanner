import hashlib 
import itertools 

# Finding out if files hash values are the same 
userFilesListName = []
while True:
	try:
		userFile = input("Print here the name of your file with extension (e.g myFile.txt) -- > ")
		if len(userFile.split(".")) != 2:
			raise 
		userFilesListName.append(userFile)
		
		if len(userFilesListName) >= 2:
			#Asking the user if he has any other files that he wants to add 
			userQuestion = input("Do you have any other files that you would like to add ? -- > ")
			if userQuestion == "yes" or userQuestion == "Yes":
				continue 
			elif userQuestion == "no" or userQuestion == "No":
				break 
			else:
				raise 
	except:
		for i in range(3):
			print() 
		
		print("Please answer correctly to the question !")
		print("Try again !")
		
		for i in range(3):
			print() 
			
		continue
		
FILE_PERMUTATIONS_LIST = itertools.permutations(userFilesListName, 2)
FILE_SAME_LIST = []

for element in FILE_PERMUTATIONS_LIST:
	with open(element[0], "rb") as f1, open(element[1], "rb") as f2:
		if hashlib.sha1(f1.read()).digest() == hashlib.sha1(f2.read()).digest():
			FILE_SAME_LIST.append([element[0], element[1]])
		else:
			continue 

print("This is a list with all the files that are the same from the files that you gave -- > {0}".format(FILE_SAME_LIST))