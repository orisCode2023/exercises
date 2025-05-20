
def sortColors(nums):
    idx = i = color = 0
    while color < 3:
        if nums[i] == color:
            nums[i], nums[idx] = nums[idx], nums[i]
            idx += 1
        i += 1
        if i == len(nums):
            color += 1
            i = idx

    print(nums)


sortColors([1,2,0,2,2,1,0])