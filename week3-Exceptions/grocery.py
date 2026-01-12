'''1.Suppose that you’re in the habit of making a list of items you need from the grocery store.'''
'''2.n a file called grocery.py, implement a program that prompts the user for items, one per line, 
until the user inputs control-d (which is a common way of ending one’s input to a program).
 3.Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
 4. No need to pluralize the items.
5. Treat the user’s input case-insensitively.'''



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