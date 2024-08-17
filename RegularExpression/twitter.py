import re

def main():
    twt_url = input("What's your twitter's URL? ").strip()
    # user_name = get_user_name(twt_url)
    user_name = get_user_name_2(twt_url)
    print(f"Username: {user_name}")

def get_user_name_1(twt_url):
    twt_url = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", twt_url)
    return twt_url

def get_user_name_2(twt_url):
    if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", twt_url, re.IGNORECASE):
        print(f"Username:", matches.group(1))
    return twt_url
         
if __name__ == "__main__":
    main()