# не решено

import sys

def main():
    nums = list(map(int, input().split()))
    sorted_nums = sorted(nums, reverse=False)
    if nums[1] == nums[2] or nums[1] == [3]:
        print('NO')
    elif sorted_nums == nums:
        print('YES')
    else:
        print('NO')
    pass

if __name__ == '__main__':
    main()