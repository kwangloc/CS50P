from validator_collection import checkers
    
def main():
    email_inp = input("What's your address email? ")
    if check_valid_email(email_inp) == True:
        print("Valid")
    else:
        print("Invalid")

def check_valid_email(email_inp):
    return checkers.is_email(email_inp)
    
if __name__ == "__main__":
    main()
