#!/usr/bin/env python3

from person import Person
from time import perf_counter
from numba import njit

@njit
def fib_py():
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(-2))

def main():
	f = Person(51)
	print(f.getAge())
	print(f.getDecades())

	for i in range(20, 31):
		start = perf_counter()
		print(f.fib(45))
		end = perf_counter()
		print(f"time for fib_py(50): {end-start}")


if __name__ == '__main__':
	main()

"""
time for fib_py(45): 18.178770376369357
time for fib_numba(45): 18.045608339831233


"""
