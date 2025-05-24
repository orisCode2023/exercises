haystack = "mississippi"
needle = "issip"
def find_str_in_str():
    idx = 0
    start = 0

    i = 0
    while i < len(haystack):
        if needle[idx] == haystack[i]:
            if idx == 0:
                start = i
            idx += 1
            if idx == len(needle):
                return start
            i += 1
        else:
            if idx > 0:
                # Backtrack: restart from the position after where we started matching
                i = start + 1
                idx = 0
            else:
                i += 1

    return -1

print(find_str_in_str())