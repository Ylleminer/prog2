"""
Solutions to MA4
Student: John Yledahl
Reviewed by: Stefanos Tsampanakis
Reviewed date: 2024-05-20
"""
import matplotlib.pyplot as plt
import random
import math


def findPi(n):
    xout = []
    yout = []

    xin = []
    yin = []

    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2+y**2 <= 1:
            xin.append(x)
            yin.append(y)
        else:
            xout.append(x)
            yout.append(y)

    plt.scatter(xout, yout, color="blue")
    plt.scatter(xin, yin, color="red")

    print(f"\nresults for n = {n}")
    print(4*(len(xin)/n))
    print(math.pi)
    plt.savefig(f"{n}-dots.png")
    plt.show()



def main():
    findPi(1000)
    findPi(10000)
    findPi(100000)


if __name__ == "__main__":
    main()