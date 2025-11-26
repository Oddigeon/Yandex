import sys

def main():
    nums = list(map(int, input().split()))
    count = 0
    if len(nums) < 3:
        print(0)
        return
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
            count += 1
    print(count)
    pass

if __name__ == '__main__':
    main()