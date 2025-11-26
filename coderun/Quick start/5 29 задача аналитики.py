import sys 

def main():
    a, b, c = map(int, input().split())
    d = b**2 - 4 * a * c
    if d < 0:
        print(0)
    elif d == 0:
        print(1)
        print((-b) / (2 * a))
    elif d > 0:
        k1 = ((-b) - (d**0.5)) / (2 * a)
        k2 = ((-b) + (d**0.5)) / (2 * a)
        print(2)
        print(k1, k2)
    pass

if __name__ == '__main__':
    main()