import hashlib 

def errorMessage():
	for i in range(3):
		print() 
		
	print("Please answer correctly to the question !")
	print("Try again !")
	
	for i in range(3):
		print() 

while True:
	print("Choose the algorithm of your hash code.")
	print("1. MD5 128 bit -- > UTF16")
	print("2. SHA-1 160 bit -- > UTF20")
	print("3. SHA-224 224 bit -- > UTF28")
	print("4. SHA-256 256 bit -- > UTF32")
	print("5. SHA-384 384 bit -- > UTF48")
	print("6. SHA-512 512 bit -- > UTF64")
	userALGORITHM = input("Print here the number of the algorithm that you want to code -- > ")
	try:
		userALGORITHM = eval(userALGORITHM)
		if userALGORITHM not in list(range(1, 7)):
			raise 
		else:
			break 
	except:
		errorMessage()		

class _algorithm:
	def __init__(self, user_Algorithm):
		self.algorithm = user_Algorithm
		self.utf = None 
	def calculate_HASH(self):
		self.userString = input("Print here your string -- > ")
		if self.algorithm == "md5":
			self.userHASH = 	hashlib.md5(self.userString.encode())
		elif self.algorithm == "sha-1":
			self.userHASH = hashlib.sha1(self.userString.encode())
		elif self.algorithm == "sha-224":
			self.userHASH = hashlib.sha224(self.userString.encode())
		elif self.algorithm == "sha-256":
			self.userHASH = hashlib.sha256(self.userString.encode())
		elif self.algorithm == "sha-384":
			self.userHASH = hashlib.sha384(self.userString.encode())
		elif self.algorithm == "sha-512":
			self.userHASH = hashlib.sha512(self.userString.encode())
		return self.userHASH

for i in range(3):
	print ()
	
if userALGORITHM == 1:
	#MD5 128 bit -- > UTF16 
	myUserHASH = _algorithm("md5")
	_userHASH = myUserHASH.calculate_HASH()
	print("Your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, _userHASH.digest()))
	print("Your string {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, _userHASH.hexdigest()))
	print("The length of your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, len(_userHASH.digest())))
	print("The length of your string {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, len(_userHASH.hexdigest()))) 
elif userALGORITHM == 2:
	#SHA-1 160 bit -- > UTF20 
	myUserHASH = _algorithm("sha-1")
	_userHASH = myUserHASH.calculate_HASH()
	print("Your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, _userHASH.digest())) 
	print("Your string {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, _userHASH.hexdigest()))
	print("The length of your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString,  len(_userHASH.digest()))) 
	print("The length of your string {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, len(_userHASH.hexdigest()))) 
elif userALGORITHM == 3:
	#SHA224 244 bit -- > UTF28
	myUserHASH = _algorithm("sha-224")
	_userHASH = myUserHASH.calculate_HASH()
	print("Your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, _userHASH.digest()))
	print("Your string {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, _userHASH.hexdigest()))
	print("The length of your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, len(_userHASH.digest())))	
	print("The length of your string {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, len(_userHASH.hexdigest()))) 
elif userALGORITHM == 4:
	#SHA256 256bit -- > UTF32 
	myUserHASH = _algorithm("sha-256")
	_userHASH = myUserHASH.calculate_HASH() 
	print("Your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, _userHASH.digest()))
	print("Your string {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, _userHASH.hexdigest()))
	print("The length of your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, len(_userHASH.digest())))
	print("The length of your string {0} in HASH CODE hexadecimal digest is -- >{1}".format(myUserHASH.userString, len(_userHASH.hexdigest())))
elif userALGORITHM == 5:
	#SHA384 384 bit -- > UTF48
	myUserHASH = _algorithm("sha-384")
	_userHASH = myUserHASH.calculate_HASH()
	print("Your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, _userHASH.digest()))
	print("Your string  {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, _userHASH.hexdigest()))
	print("The length of your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, len(_userHASH.digest())))
	print("The length of your string {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, len(_userHASH.hexdigest())))
elif userALGORITHM == 6:
	#SHA-512 512 bit -- > UTF64
	myUserHASH = _algorithm("sha-512")
	_userHASH = myUserHASH.calculate_HASH()
	print("Your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, _userHASH.digest()))
	print("Your string {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, _userHASH.hexdigest()))
	print("The length of your string {0} in HASH CODE binary digest is -- > {1}".format(myUserHASH.userString, len(_userHASH.digest())))
	print("The length of your string {0} in HASH CODE hexadecimal digest is -- > {1}".format(myUserHASH.userString, len(_userHASH.hexdigest())))