import hashlib

# User file ask
while True:
	print("test")
	firstFile = input("Print here the name of your first file with extension (e.g myfile.txt) -- > ")
	secondFile = input("Print here the name of your second file with extension (e.g myfile.txt) -- > ") 
	try:
		with open("{0}".format(firstFile), "rb") as f1, open("{0}".format(secondFile), "rb") as f2:
			if hashlib.sha224(f1.read()).digest() == hashlib.sha224(f2.read()).digest():
				print("The files are the same")
			else:
				print("The files are different !")
		
		break
	except:
		for i in range(3):
			print() 
			
		print("Please answer correctly to the question !")
		print("Try again !")
		
		for i in range(3):
			print() 
		
		continue 
		
