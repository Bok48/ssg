
from textnode import TextType, TextNode

def main():
    textnode = TextNode("A link", TextType("link"), "http://localhost:8888")

    print(textnode)


main()