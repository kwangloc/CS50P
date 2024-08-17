import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'^<iframe(?:\swidth="[0-9]+")?(?:\sheight="[0-9]+")?\ssrc="([\w0-9:/\.]+)"(?:\stitle="[\w\W]+")?(?:\sframeborder="[0-9]+")?(?:\sallow="[\w\W]+")?(?:\sallowfullscreen)?></iframe>$'
    if matches := re.search(pattern, s, re.IGNORECASE):
        original_url = matches.group(1)
        sub_pattern = r"^https?://(?:www\.)?youtube\.com/embed/([\w0-9]+)$"
        if sub_matches := re.search(sub_pattern, original_url, re.IGNORECASE):
            token = sub_matches.group(1)
            short_url = "https://youtu.be/" + token
            return short_url            
    else:
        return None

if __name__ == "__main__":
    main()
