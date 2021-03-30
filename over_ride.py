class Employee:
	raise_amount=1.05
	def __init__(self,first=None,last=None,salary=None):
		self.first=first
		self.last=last
		self.salary=salary
	def getdata(self):
		first=input("enter firstname:")
		last=input("enter  lastname:")
		salary=int(input("enter salary:"))
		self.__init__(first,last,salary)

	def payraise(self):
		return self.salary*self.raise_amount
	def displaydetails(self):
		for i in self.__dict__:
			print(i," : ",self.__dict__[i])

class Developer(Employee):
	raise_amount=1.09
	def payraise(self):
		return self.salary*self.raise_amount
class Manager(Employee):
	raise_amount=1.5
	def payraise(self):
		return self.salary*self.raise_amount

while True:
	print("--"*20)
	print("1 --enter employee data")
	print("2 --enter developer data")
	print("3 --enter manager data")
	print("4 --print employee  raise salary")
	print("5 -- print Developer raise salary")
	print("6 -- print Manager raise salary")
	print("7 --exit")


	n=int(input("enter choice:"))
	if n==1:
		emp_1=Employee()
		emp_1.getdata()
		print('*'*20)
		print("employee details")
		emp_1.displaydetails()
	elif n==2:
		emp_2=Developer()
		emp_2.getdata()
		print('*'*20)
		emp_2.displaydetails()
	elif n==3:
		emp_3=Manager()
		emp_3.getdata()
		print('*'*20)
		emp_3.displaydetails()
	elif n==4:
		print("raised salary of emp_1 is:",emp_1.payraise())
	elif n==5:
		print("raised salary of developer:",emp_2.payraise())
	elif n==6:
		print("raised salary of manager:",emp_3.payraise())
	elif n==7:
		print("exit")
		break
