def main():
    outdated()

def outdated():
    dict_date = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    while True:
        try:
            text_input = input("Date: ")
            temp_store = text_input.split('/')
            if len(temp_store) == 3:
                day = int(temp_store[1])
                month = int(temp_store[0])
                year = int(temp_store[2])
                if day <= 31 and month <= 12:
                    print(f"{year}-{month:02}-{day:02}")
                    break
            else:
                temp_store = text_input.split(" ")
                day = temp_store[1]
                month = temp_store[0].capitalize()
                year = int(temp_store[2])
                if day[len(day)-1] == ',':
                    day = int(day.strip(","))
                    if day <= 31 and month in dict_date:
                        print(f"{year}-{dict_date[month]:02}-{day:02}")
                        break
        except (ValueError, IndexError):
            pass
        else:
            pass

main()