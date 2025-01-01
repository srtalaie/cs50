import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.strip()
    search = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(search)


if __name__ == "__main__":
    main()
