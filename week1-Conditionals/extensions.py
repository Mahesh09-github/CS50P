def main():
    file_format=input("Files: ")
    media_type(file_format)

def media_type(n):
    if n.endswith(".gif"):
        print("image/gif")
    elif n.endswith(".jpeg") or n.endswith(".jpg"):
        print("image/jpeg")
    elif n.endswith(".png"):
        print("image/png")
    elif n.endswith(".pdf"):
        print("applicaton/pdf")
    elif n.endswith(".txt"):
        print("tect/plain")
    elif n.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octetstream")

main()