# You should never expect your users to always follow your hopes for clean input. 
# Indeed, users will often violate your intentions as a programmer.
import re

def main():
    email_inp = input("What's your name?").strip()
    print(reformat_user_email(email_inp))

def reformat_user_email(email):
    if matches := re.search(r"^(.+), (.+)$", email):
        # last, first = matches.groups()
        # email = f"{first} {last}"
        # or
        # last = matches.group(1)
        # first = matches.group(2)
        # email = f"{first} {last}"
        # or
        email = matches.group(2) + " " + matches.group(1)
    return email

if __name__ == "__main__":
    main()