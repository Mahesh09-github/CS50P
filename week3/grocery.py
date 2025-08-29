def main():
    grocery={}
    while True:
        try:
            user_input=input("Item: ")
            if user_input.upper() in grocery:
                user_input=user_input.upper()
                grocery[user_input]+=1
            else:
                user_input=user_input.upper()
                grocery[user_input]=1
        except EOFError:
            grocery=dict(sorted(grocery.items()))
            for key in grocery:
                print(f"{grocery[key]} {key}",end="\n")
            break
main()

# better version
# def main():
#     grocery = {}
#     while True:
#         try:
#             item = input("Item: ").upper()
#             grocery[item] = grocery.get(item, 0) + 1   # increment count safely
#         except EOFError:
#             # Print sorted by keys
#             for key in sorted(grocery.keys()):
#                 print(f"{grocery[key]} {key}")
#             break

# main()