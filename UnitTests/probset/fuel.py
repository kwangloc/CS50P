def main():
    inp = input("Fraction: ")
    print(gauge(convert(inp)))

def convert(fraction):
    try:
        numerator, denominator = fraction.split("/")
        numerator = int(numerator)
        denominator = int(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        if numerator > denominator:
            raise ValueError
        return round(numerator/denominator*100)
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if 0 <= percentage <= 100:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{percentage}%"


if __name__ == "__main__":
    main()