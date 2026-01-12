def main():
    s=input("Input: ")
    result=shorten(s)
    print(f"Output: {result}")

def shorten(s):
    result=""
    vowels=""
    for c in s:
        if c in ["a","e","i","o","u"]:
            vowels+=c
        else:
            result+=c
    return result

if __name__ == "__main__":
    main()