import sys
import csv
def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("too many command-line arguments")
        if not sys.argv[1].endswith(".csv"):
            sys.exit("not a CSV file")
        filename = sys.argv[1]
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                last, first = row["name"].split(",")
                students.append({"first": first.strip(), "last": last.strip(), "house": row["house"]})
        with open(sys.argv[2], 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()