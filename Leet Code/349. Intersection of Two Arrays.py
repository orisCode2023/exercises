def sol():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    st = set()
    for num in nums2:
        if num in nums1:
            st.add(num)
    lst = list(st)
    return lst

print(sol())

