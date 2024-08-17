def main():
    txt = input("Input: ")
    print("Output:", twttr(txt))
    # twttr(txt)

def twttr(txt):
    out = ""
    for i in txt:
        if i != 'u' and i != 'e' and i != 'o' and i != 'a' and i != 'i' and i != 'U' and i != 'E' and i != 'O' and i != 'A' and i != 'I':
            out += i
    return out

main()