"""
Solutions to MA4
Student: John Yledahl
Reviewed by: Stefanos Tsampanakis
Reviewed date: 2024-05-20
"""
#!/usr/bin/env python3

from person import Person
from time import perf_counter
from numba import njit
import matplotlib.pyplot as plt


def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
	

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))


def main():
	#print(fib_numba(47))
	f = Person(25)
	#print(f.fib(47))

	print(f.getAge())
	print(f.getDecades())

	coords = []
	for i in range(20, 40):
		start = perf_counter()
		fib_py(i)
		end = perf_counter()
		coords.append(end-start)
	plt.plot([ii for ii in range(20, 40)], coords)
	print(f"time for fib_py(39){coords[-1]}")

	coords = []
	for i in range(20, 40):
		start = perf_counter()
		fib_numba(i)
		end = perf_counter()
		coords.append(end-start)
	plt.plot([ii for ii in range(20, 40)], coords)
	print(f"time for fib_numba(39){coords[-1]}")

	coords = []
	for i in range(20, 40):
		f = Person(i)
		start = perf_counter()
		f.fib(i)
		end = perf_counter()
		coords.append(end-start)
	plt.plot([ii for ii in range(20, 40)], coords)
	print(f"time for f.fib(39){coords[-1]}")
	plt.legend(["fib_py", "fib_numba", "f.fib"])
	plt.savefig("fib_test_20-39")
	plt.show()
	


if __name__ == '__main__':
	main()


"""
time for fib_py(39)10.421483899999998
time for fib_numba(39)0.49612114499996096
time for f.fib(39)0.550219052999978
f.fib(47) returns a negative value because of integer overflow: -1323752223
"""
