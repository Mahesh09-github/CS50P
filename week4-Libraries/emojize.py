import emoji
def emo():
    response="yes"
    while response=="yes":
        user_input=input("Input:")
        print(emoji.emojize(f"Output:{user_input}"))
        response=input("Again?:")

emo()