import re
import sys


def main():
    print(parse(input("HTML: ")))#input=<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
    #<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0"
    #  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    #<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>



def parse(s):
    if match:=re.search(r'^<iframe(?:[a-zA-Z0-9="" ])*src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})"[ ](?:[a-zA-Z0-9=""; ]).*></iframe>$',s):
        if "https"in s:
            return f"https://youtu.be/{match.group(1)}"
        else:
            return f"http://youtu.be/{match.group(1)}"
    return None





if __name__ == "__main__":
    main()