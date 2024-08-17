def main():
    inp = input("What time is it? ")
    time_float = convert(inp)
    if 7.0 <= time_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")

def convert(time):
    tmp_li = time.split(":")
    hour = float(tmp_li[0])
    minute = float(tmp_li[1])
    return hour + minute/60

if __name__ == "__main__":
    main()