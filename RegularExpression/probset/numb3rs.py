import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # if matches := re.search(r"^(\w+)\.(\w+)\.(\w+)\.(\w+)$", ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        # if 0 <= (int(matches.group(1)) and int(matches.group(2)) and int(matches.group(3)) and int(matches.group(4))) <= 255:
        flag = True
        for group in matches.groups():
            if int(group) > 255 or int(group) < 0:
                flag = False
        return flag
    return False

if __name__ == "__main__":
    main()