def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_letters(s) and string_size(s) and check_numbers(s) and special_characters(s):
        return True
    else:
        return False


def check_letters(t):
        if t[:2].isalpha():
            return True
        else:
            return False

def string_size(u):
    if 2<=len(u)<=6:
        return True
    else:
        return False

def check_numbers(v):
    if not v[-1].isdigit():
        return False
    for ch in v:
        if ch.isdigit():
            if ch=="0":
                return False
            else:
                return True
    return True
def special_characters(x):
    if x.isalnum():
        return True
    else:
        return False
main()