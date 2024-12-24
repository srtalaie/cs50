import csv
import sys

students = []

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"].split(", ")
                first_name = name[1]
                last_name = name[0]
                house = row["house"]
                student = {"first": first_name, "last": last_name, "house": house}
                students.append(student)
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(
                    {
                        "first": student["first"],
                        "last": student["last"],
                        "house": student["house"],
                    }
                )
except FileNotFoundError:
    sys.exit("File does not exist")
