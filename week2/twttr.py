def main():
    s=input("Input: ")

    result=""
    vowels=""
    for c in s:
        if c in ["a","e","i","o","u"]:
            vowels+=c
        else:
            result+=c
    print(f"Output: {result}")

main()