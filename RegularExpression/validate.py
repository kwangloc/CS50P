import re
    
def main():
    while(True):
        email = input("What's your email? ").strip()
        if is_email(email) == True:  
            break
    
def is_email(email):
    # extension = ""
    # for i in range(len(email)-1, -1, -1):
    #     if (email[i] == "@"):
    #         extension = email[i:]
    # if extension == "@gmail.com":
    #     return True
    # return False
    # if re.search(".@.", email): # _@_   (_ means >= 1)
    # if re.search(".*@.*", email): # @
    # if re.search("*@*", email): # error
    # if re.search(".+@.+", email): # _@_
    # if re.search(r"^.+@.+\.edu$", email):
    # if re.search(r"^[^@]+@[^@]+\.edu$", email, re.IGNORECASE):
        # ^ match from the start of the string
        # $ match at the end of the string
        # [^@] any characters except "@"
        # + one or more of the things to the left
        # @ just a character that must appear in the string
        # \ escape character, tell the interpreter to treat the next character as a raw character 
        # (in this context mean the string must end with ".edu")
    # if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    # if re.search(r"^\w+@\w+\.(edu|com|gov|net)$", email, re.IGNORECASE):
    # if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov|net)$", email, re.IGNORECASE):
    if re.search(r"^\w+@(\w+\.)*\w+\.(edu|com|gov|net)$", email, re.IGNORECASE):
        return True
    return False

if __name__ == "__main__":
    main()


