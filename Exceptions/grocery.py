def main():
    grocery()

def grocery():
    grocery_dict = {}
    try:
        while True:
            item = input().upper()
            if item == "0":
                break
            if item in grocery_dict:
                grocery_dict[item] += 1
            else:
                grocery_dict[item] = 1
    except EOFError:
        pass
    else:
        myKeys = list(grocery_dict.keys())
        myKeys.sort()
        sorted_dict = {i: grocery_dict[i] for i in myKeys}
        for j in sorted_dict:
            print(sorted_dict[j], j)

main()