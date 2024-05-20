"""
Solutions to MA4
Student: John Yledahl
Reviewed by: Stefanos Tsampanakis
Reviewed date: 2024-05-20
"""
import random
import math
from time import perf_counter

def hypersphere(n, d):
    coordinates = [[random.uniform(-1, 1) for j in range(d)] for i in range(n)]
    # checks the coordinates distance from origo in a d-dimesional space
    # applies x1^2 + x2^2 + ... + xd^2
    coordSUMS = [sum(list(map(lambda x : x**2, i))) for i in coordinates]

    # checks if the coordinate is within the d-dimesional hypersphere
    # and puts it either outside or inside
    coordIN = list(filter(lambda x: x<=1, coordSUMS))
    #coordOUT = list(filter(lambda x: x>1, coordSUMS))

    print(f"results for {n} points in a {d}-dimesional hypersphere")
    print(2**d*(len(coordIN)/len(coordinates)))

def hypersphere_exact(r, d):
    return (math.pi**(d/2)/math.gamma(d/2 + 1)) * r**d


def main():
    start = perf_counter()
    hypersphere(10000000, 11)
    end = perf_counter()

    print(f"time for 10000000 points in 11-dimensional hypersphere")
    print(end-start)


if __name__ == "__main__":
    main()

"""
time for 10000000 points in 11-dimensional hypersphere
53.61117279899918
"""