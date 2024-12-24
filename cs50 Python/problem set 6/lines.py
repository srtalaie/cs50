import sys

line_count = 0

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        with open(sys.argv[1], "r") as file:
            for line in file:
                if line.lstrip().startswith("# "):
                    pass
                elif line.isspace():
                    pass
                else:
                    line_count += 1
            print(line_count)
except FileNotFoundError:
    sys.exit("File does not exist")
