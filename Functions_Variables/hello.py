# # escape character 
# # name = input("\"What is your name?\" ") 
# # using string build-in methods 
# # name = name.strip()
# # name = name.capitalize()
# # name = name.title()
# name = input("\"What is your name?\" ") .strip().title()
# # split a string into substrings, assign multiple var
# first, last = name.split(" ")
# # override 
# print("hello,", end = "$$$")
# print(name)
# # format string
# print(f"hello, {first}")

# """"
# Comments 
# in multiple-lines
# """

## int
# x = int(input("x = "))
# y = int(input("y = "))
# # z = int(x) + int(y)
# print("x + y =", x+ y)

# float

# x = float(input("x = "))
# y = float(input("y = "))
# z = round(x+y)
# print(f"{z:,}")

## definition function

# def main():
#     name = input("What's your name?")
#     hello(name)

# def hello(to = "world"):
#     print("Hello,", to)

# main()

# return

def main():
    x = int(input("x = "))
    print("x squared is", square(x))

def square(n):
    return n*n

main()