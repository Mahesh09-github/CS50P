def main():
    User_input=input("String: ")
    if User_input[-3] in ["a","e","i","o","u"]:
        print("it is a vowel")
    else:
        print("it is not a vowel")

main()