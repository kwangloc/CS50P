import sys
import datetime
import inflect

p = inflect.engine()

def main():
    dob_inp = input("Date of Birth: ")
    try:
        print(count_minutes(dob_inp))
    except ValueError:
        sys.exit("Valid input")

def count_minutes(dob_inp):
    year, month, day = dob_inp.split("-")
    datetime_dob = datetime.date(int(year), int(month), int(day))
    days_difference = datetime.date.today()-datetime_dob
    minutes_difference = days_difference.days*24*60
    return f"{p.number_to_words(minutes_difference).replace('and ', '').capitalize()} minutes"

if __name__ == "__main__":
    main()