def main():
    inp = input()
    print(convert(inp))

def convert(text_emoji):
    tmp_str = text_emoji.split()
    for i in range(len(tmp_str)):
        if tmp_str[i] == ':)':
            tmp_str[i] = "🙂"
        elif tmp_str[i] == ':(':
            tmp_str[i] = "🙁"
    return ' '.join(tmp_str)

if __name__ == "__main__":
    main()