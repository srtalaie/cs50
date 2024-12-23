def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    plate_len = len(s)

    # Must be at least 2 characters long and no more than 6
    if plate_len > 6 or plate_len < 2:
        return False

    # First 2 characters must be a letter
    for i in range(2):
        if s[i] in nums:
            return False

    # Check if there are any special characters
    if not (s.isalnum()):
        return False

    # First number cannot be a 0
    for i in range(plate_len):
        if s[i] in nums:
            for j in range(len(s[0:i])):
                if s[j] == str(0):
                    return False

    # Numbers cannot be in the middle
    # zipping list of string s and string s beginning at s[1] will create tuples of each value and it's adjacent sibling
    for x, y in zip(list(s), list(s[1:])):
        if x.isnumeric() and y.isalpha():
            return False

    return True


if __name__ == "__main__":
    main()
