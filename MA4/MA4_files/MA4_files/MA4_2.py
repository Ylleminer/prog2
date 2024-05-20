#!/usr/bin/env python3

from person import Person
from time import perf_counter
from numba import njit
import matplotlib.pyplot as plt


def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(-2))
	

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(-2))


def main():
	f = Person(51)
	print(f.getAge())
	print(f.getDecades())

	coords = []
	for i in range(20, 40):
		start = perf_counter()
		fib_py(i)
		end = perf_counter()
		coords.append(end-start)
	plt.plot([ii for ii in range(20, 40)], coords)

	coords = []
	for i in range(20, 40):
		start = perf_counter()
		fib_numba(i)
		end = perf_counter()
		coords.append(end-start)
	plt.plot([ii for ii in range(20, 40)], coords)

	coords = []
	for i in range(20, 40):
		start = perf_counter()
		f.fib(i)
		end = perf_counter()
		coords.append(end-start)
	plt.plot([ii for ii in range(20, 40)], coords)
	plt.legend(["fib_py", "fib_numba", "f.fib"])
	plt.show()


if __name__ == '__main__':
	main()


"""
time for fib_py(45): 18.178770376369357
time for fib_numba(45): 18.045608339831233


"""
