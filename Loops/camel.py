camelCase = input("camelCase: ")
snake_case = ""
for i in camelCase:
    if 65 <= ord(i) <= 90:
        snake_case += "_" + chr(ord(i) + 32)
    else:
        snake_case += i
print("snake_case:", snake_case)

