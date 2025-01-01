import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    if re.search(r"^<iframe(?:.)*><\/iframe>$", s, re.IGNORECASE):
        url = re.search(
            r"(?:http(?:s)*):\/\/(?:www\.)*youtube\.com\/embed\/([a-zA-Z0-9]+)",
            s,
            re.IGNORECASE,
        )
        if url:
            return f"https://youtu.be/{url.group(1)}"
        else:
            return None


if __name__ == "__main__":
    main()
