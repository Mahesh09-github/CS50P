import validators
def main():
    print(is_valid_email(input("Enter your email: ")))
def is_valid_email(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"
if __name__ == "__main__":
    main()