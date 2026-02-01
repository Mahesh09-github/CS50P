import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip_address:= re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip):
        for i in range(1,5):
            if not 0 <=int(ip_address.group(i)) <=255:
                return False
        return True
    else:
        return False
    


...


if __name__ == "__main__":
    main()