"""
this code check the most appears in arr without Hash map
and with complexity of O of 1
"""
from typing import List


def majority_element(nums: List[int]) -> int:
    candidate = 0
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate