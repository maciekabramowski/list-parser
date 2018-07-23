from html.parser import HTMLParser
import pprint

x = "initial"


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):

        global x

        ha = open("final.txt","a")


        if tag == 'li':
            x = "li"
            ha.write("<" + str(tag) + ">")

        if x == "li":
            ha.write("<" + str(tag) + ">")


    def handle_endtag(self, tag):

        global x

        ha = open("final.txt","a")

        if tag == "ul":
            ha.write("\n" + "-----------------" "\n")
        if x == "li":
            ha.write("</" + str(tag) + ">")
        if tag == "li":
            x = "initial"



    def handle_data(self, data):
        global x

        ha = open("final.txt","a")

        if x == "li":
            ha.write( str(data) )
            # x = "initial"


def main():
    parser = MyHTMLParser()
    f = open("list.html", encoding="utf8")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)

if __name__ == "__main__":
    main()
