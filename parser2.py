from html.parser import HTMLParser
import pprint


class MyHTMLParser(HTMLParser):
    # def handle_starttag(self, tag, attrs):
    #     #ha = open("hemplinks.txt", "a")
    #
    #
    #     if tag == 'li':
    #         x = "li"

    def handle_data(self, data):




            ha = open("all.txt","a")
            ha.write(data)

        # ha.write(data)
        # print(data)



def main():
    parser = MyHTMLParser()
    f = open("list.html", encoding="utf8")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)

if __name__ == "__main__":
    main()
