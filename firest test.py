x = True
y = True
z = False
print(3,14,56, sep="/" , end="-")
print(x or y and z)

print((70 * (70 > 100)) + (100 * (100 > 70)))
print((4 * (4 > 2)) + (2 * (2 > 4)))
print((5 * (5 > 5)) + (5 * (5 > 5)))


a = str(bool(str(int(8.99))))
print(a + str(float(9)))