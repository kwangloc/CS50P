def main():
    txt = input("Input: ")
    print("Output:", shorten(txt))

def shorten(word):
    vowels = ['u', 'e', 'o', 'a', 'i']
    out = ""
    for i in word:
        if i.lower() not in vowels:
            out += i
    return out

if __name__ == "__main__":
    main()