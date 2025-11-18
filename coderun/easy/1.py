import sys

def main():
    numbers = [int(x) for x in input().split()]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers[1])

    pass


if __name__ == '__main__':
    main()