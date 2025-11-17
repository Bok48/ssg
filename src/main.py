
from textnode import TextType, TextNode

def main():
    textnode = TextNode("A link", TextType.LINK, "http://localhost:8888")

    print(textnode)


if __name__ == "__main__":
    main()