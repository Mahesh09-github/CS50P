import sys
import csv
import tabulate
def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("too many command-line arguments")
        if not sys.argv[1].endswith(".csv"):
            sys.exit("not a CSV file")
        filename = sys.argv[1]
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print(reader.fieldnames)
            table = list(reader)

            print(tabulate.tabulate(table, headers="keys", tablefmt="grid"))
    except Exception as e:
        sys.exit(f"Error: {e}")
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()