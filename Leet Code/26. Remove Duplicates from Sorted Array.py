arr = [1, 2, 3, 3, 4, 5, 6, 3, 7, 8, 1, 9, 2, 10]


def remove_duplicates(nums):
    nums.sort()
    for i in range(len(nums)):
        if i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
    return len(nums)


print(remove_duplicates(arr))
