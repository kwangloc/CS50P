x = int(input("x = "))
y = int(input("y = "))

# if x > y:
#     print("x > y")
# elif x < y:
#     print("x < y")
# else:
#     print("x == y")

# print((x > y) ? "x > y" : ((x < y) ? "x < y" : "x == y"))

if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")