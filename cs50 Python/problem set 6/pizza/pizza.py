import csv
import sys

from tabulate import tabulate

table = []

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]
                small_price = row[1]
                large_price = row[2]
                table.append([name, small_price, large_price])
            headers = table[0]
            table = table[1:]
        print(tabulate(table, headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
