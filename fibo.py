import time

def timeit(func):
	def timed(*args):
		print("Before the timeit  decorator")
		start_time=time.time()
		result=func(*args)
		end_time=time.time()


		min,sec=divmod((end_time-start_time),60)
		print(min,sec)
		print("time taken %8.2f * 10 exp  6"%((end_time-start_time)*10**6))
		print("after the timeit decorator")
		return result
	return timed


@timeit
def fib(n):
	a,b,i=0,1,0
	while (i<n):
		yield a
		a,b=b,a+b
		i+=1

n=int(input("enter number of fib terms:"))
f1=fib(n)
for i in range(n):
	print(f1.__next__())
