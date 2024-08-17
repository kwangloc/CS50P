list_name = []
while True:
    try:
        name = input("Name: ")
        list_name.append(name)
    except EOFError:
        greeting = "Adieu, adieu, to "
        if len(list_name) == 1 or len(list_name) == 2:
            greeting += list_name[0] + ' '
        elif len(list_name) > 2:
            for i in range(len(list_name)-1):
                greeting += list_name[i] + ', '
        if len(list_name) >= 2:
            greeting += "and " + list_name[len(list_name)-1]
        print(greeting)
        break
