from html.parser import HTMLParser
import pprint

x = "initial"

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):

        global x

        if tag == 'li':
            x = "li"

    def handle_endtag(self, tag):

        if tag == "ul":
            ha = open("final.txt","a")
            ha.write("\n" + "-----------------" "\n")


    def handle_data(self, data):
        global x

        ha = open("final.txt","a")

        if x == "li":
            ha.write("<li>" + data + "</li>")
            x = "initial"


def main():
    parser = MyHTMLParser()
    f = open("list.html", encoding="utf8")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)

if __name__ == "__main__":
    main()
