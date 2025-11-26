import sys 

def main():
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())
    if x1 + x2 < x3 or x1 + x3 < x2 or x2 + x3 < x1:
        print('NO')
    else:
        print('YES')
    pass

if __name__ == '__main__':
    main()