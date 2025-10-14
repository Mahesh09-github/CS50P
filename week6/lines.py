from fileinput import filename
import sys

def main():
    try:
        line_count = checking(sys.argv[1])
        print(f"Number of lines in {sys.argv[1]}: {line_count}")
    except IndexError:
        print("Too few command-line arguments provided.")
        sys.exit(0)
    except FileNotFoundError:
        print(f"File not found: {sys.argv[1]}")
        sys.exit(1)

def checking(filename):
        if len(sys.argv) != 2:
            print("Too many arguments")
            sys.exit(1)
        if filename.endswith(".py") == False:
            print("Not a Python file")
            sys.exit(1)
        filename = sys.argv[1]
        line_count = count_lines(filename)
        return line_count

def count_lines(filename):
    with open(filename, 'r',encoding='utf-8') as file:
        file_contents = file.read()
        return sum(1 for line in file_contents.splitlines() if line.strip() and not line.strip().startswith('#'))

if __name__ == "__main__":
    main()