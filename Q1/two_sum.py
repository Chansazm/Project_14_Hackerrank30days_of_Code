nums = [2, 7, 9, 11, 15]
target = 11


def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(nums[i], nums[j])
                return True
    return False


def two_sum_binary(nums, target):
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            return True
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            nums[i] + nums[j] > target
            j -= 1
    return False


print(twoSum(nums, target))
print(two_sum_binary(nums, target))
