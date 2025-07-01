def find_target_index():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 4
    start = 0
    end = len(nums) - 1

    while start < end:
        middel = (end + start) // 2
        if middel == target:
            return nums.index(middel)

        if target > middel:
            start = middel + 1

        else:
            end = middel - 1

print(find_target_index())





