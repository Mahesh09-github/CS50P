def main():
    s=input("camelcase: ")
    updated=checksupperchr(s)
    n=snakecase(updated)
    print(f"snake_case: {n}")

    
def checksupperchr(s):
    result=""
    for c in s:
        if c.isupper():
            result+="_"+c
        else:
            result+=c
    return result

def snakecase(s):
    return s.lower()

main()