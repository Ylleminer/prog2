import random
import math
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import perf_counter

def hypersphere(nd):
    n = nd[0]
    d = nd[1]
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
    max_workers = 4
    inputs = [[1000000, 11] for i in range(10)]
    print(inputs)

    multistart = perf_counter()
    with ThreadPoolExecutor() as ex:
        ex.map(hypersphere, inputs)
    multiend = perf_counter()
    
    print(f"time for multi: {multiend-multistart}")

if __name__ == "__main__":
    main()

"""
ProcessPoolExecutor:
time for multi: 28.980965718001244

ThreadPoolExecutor:
time for multi: 60.74743393099925
"""