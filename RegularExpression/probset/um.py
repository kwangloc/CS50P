import re

def main():
    print(count(input("Text: ")))

def count(s):
    pattern = r"\bum\b"
    tmp_li = re.findall(pattern, s, re.IGNORECASE)
    print(tmp_li)
    return len(tmp_li)

def count_2(s):
    s = s.lower()
    count = 0
    for i in range(len(s)):
        try:
            word = s[i] + s[i+1]
            if i == 0 and word == "um":
                count += 1
            elif word == "um" and s[i-1].isalpha() == False:
                count += 1
        except IndexError:
            pass
    return count

if __name__ == "__main__":
    main()