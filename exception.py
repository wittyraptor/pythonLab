#exception handling in file opening
while  True:
	print("1--Enter the  file name source and destination")
	print("2--Open the file in read and write mode")
	print("3-- Writing to a file")
	print("4--Reading the  content in the file")
	print("5--Copying the file content to another file")
	print("6--Closing the  file")
	print("7-- exit")
	n=int(input("enter the  choice  1-7:"))
	if n==1:

		f=input('enter existing the file name:')
		f1=input('enter the new file name:')
		print('two files created')
	if n==2:
		try:
			A=open('f','r')
			B=open('f1','w')
		except FileNotFoundError:
			print('-'*20)
			print("FileNotFoundError:no such file found")
			print('-'*20)
		except NameError:
			print('-'*20)
			print("NameError:please create such file")
			print('-'*20)
		else:
			print('-'*20)
			print('operation done successfull')
			print('-'*20)
	if n==3:
		try:
			a=A.read()
			B.write(a)
		except NameError:
			print('-'*20)
			print("NameError:plz Open the file first")
			print('-'*20)
		else:
			print("file copied to B successfull")
			A.close()
			B.close()
	if n==4:
		try:
			B.read()
		except ValueError:
			print('-'*20)
			print("ValueError: Plz open the file first")
			print('-'*20)
		except NameError:
			print('-'*20)
			print("B not found")
			print('-'*20)
	if  n==5:
		try :
			A=open('f','r')
			B=open('f1','w')
			str1=A.read()
			B.write(str1)
		except IOError:
			print('-'*20)
			print("Error:can't find file")
			print('-'*20)
		except NameError:
			print('-'*20)
			print("Name error found")
			print('-'*20)
		else:
			print("file copied succesfull")
			A.close()
			B.close()
	if n==6:
		try:
			print(A/B)
		except TypeError:
			print('-'*20)
			print("TypeError: cannot do this Operations")
			print('-'*20)
		except NameError:
			print('file not found')
	if n==7:
		print('exited')
		break
