def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if check_ans(ans):
        print("Yes")
    else:
        print("No")

def check_ans(ans):
    correct_ans = ["42", "forty-two", "forty two"]
    if ans.strip().lower() in correct_ans:
        return True
    else:
        return False

if __name__ == "__main__":
    main()