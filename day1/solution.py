
def twoSum(nums, target):
    m = {}
    for i in range(len(nums)):
        m[nums[i]] = i

    for i in range(len(nums)):
        res = target - nums[i]
        if (res in m) and (m[res] != i):
            return nums[m[res]] * nums[i]
    return None


def threeSum(nums, target):
    nums.sort()
    for i, value in enumerate(nums):
        j, k = i + 1, len(nums) - 1
        while (j < k):
            tot = nums[i] + nums[j] + nums[k]
            if tot < target:
                j += 1
            elif tot > target:
                k -= 1
            else:
                return nums[i] * nums[j] * nums[k]


def threeSumItertools(nums, target):
    from itertools import combinations
    for i, j, k in combinations(nums, 3):
        if i + j + k == target:
            return i * j * k


def main():
    with open('input.txt', 'r') as f:
        input = f.read()

    nums = [int(i) for i in input.split(",")]
    target = 2020

    print("Part 1 solution: ", twoSum(nums, target))
    print("Part 2 solution: ", threeSum(nums, target))
    print("Part 2 alternative solution: ", threeSumItertools(nums, target))

    return 0


if __name__ == "__main__":
    main()
