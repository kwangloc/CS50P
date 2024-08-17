def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if 2 <= len(plate) <= 6:
        if plate[0].isalpha() and plate[1].isalpha():
            for i in range(2, len(plate)):
                if not plate[i].isalpha() and not plate[i].isdigit():
                    return False
                elif plate[i].isdigit():
                    if plate[i] == '0':
                        return False
                    else:
                        for j in range(i, len(plate)):
                            if not plate[j].isdigit():
                                return False
                        return True
            return True
        else:
            return False
    return False

if __name__ == "__main__":
    main()
