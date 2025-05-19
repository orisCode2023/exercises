def return_arr():
    end = greater_number_key = idx = maximum = 0
    dic_value = {}
    dic_index = {}
    arr = [1, 2, 2, 3, 1, 2, 4, 5, 6, 5]
    for i in range(len(arr)):
        # check if the current number in the dic
        if arr[i] in dic_value:
            # assign the counter value to plus 1
            dic_value[arr[i]] += 1
            # finding the max
            if dic_value[arr[i]] > maximum:
                maximum = dic_value[arr[i]]
                # end of the last show in the arr
                end = i
                # saving the key of the greater value
                greater_number_key = arr[i]

        else:
            # adding the value and the counter
            dic_value.update({arr[i]:1})
            # adding the index of the arr
            dic_index.update({arr[i]:i})

    print(maximum)
    print(end)
    print(dic_value)
    print(dic_index)
    start = dic_index[greater_number_key]
    new_arr = arr[start: end + 1]
    print(new_arr)
    print(len(new_arr))


def s():
    nums = [1, 2, 2, 3, 1, 2, 4, 5, 6, 5]
    greater_number_key = float('inf')  # start with the max val possible
    maximum = 0
    dic_value = {}
    dic_index = {}
    for i in range(len(nums)):
        if nums[i] in dic_value:
            dic_value[nums[i]] += 1
        else:
            dic_value.update({nums[i]: 1})
            dic_index.update({nums[i]: i})

        if dic_value[nums[i]] > maximum:
            maximum = dic_value[nums[i]]


            greater_number_key = i - dic_index[nums[i]] + 1
        elif dic_value[nums[i]] == maximum:
            greater_number_key = min(i - dic_index[nums[i]] + 1, greater_number_key)

    return greater_number_key

print(s())