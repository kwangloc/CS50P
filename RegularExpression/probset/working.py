import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern3 = r"^([0-9]+(?::[0-9]+)?)\s([\w]+)\sto\s([0-9]+(?::[0-9]+)?)\s([\w]+)$"
    if matches := re.search(pattern3, s, re.IGNORECASE):
        time_1 = matches.group(1)
        ab_1 = matches.group(2)
        time_2 = matches.group(3)
        ab_2 = matches.group(4)
        h_1 = time_1
        m_1 = "0"
        h_2 = time_2
        m_2 = "0"
        try:
            h_1, m_1 = time_1.split(":")
        except ValueError:
            pass
        try:
            h_2, m_2 = time_2.split(":")
        except ValueError:
            pass
        h_1 = int(h_1)
        m_1 = int(m_1)
        h_2 = int(h_2)
        m_2 = int(m_2)
        if (1 <= h_1 <= 12) and (1 <= h_2 <= 12) and (0 <= m_1 <= 59) and (0 <= m_2 <= 59):
            if h_1 == 12:
                if ab_1 == "AM":
                    h_1 -= 12
            else:
                if ab_1 == "PM":
                    h_1 += 12
            if h_2 == 12:
                if ab_2 == "AM":
                    h_2 -= 12
            else:
                if ab_2 == "PM":
                    h_2 += 12
            return (f"{h_1:02}:{m_1:02} to {h_2:02}:{m_2:02}")
        else:
            raise ValueError
    else:
        raise ValueError

if __name__ == "__main__":
    main()