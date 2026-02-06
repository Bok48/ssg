import sys

from generate_page import(
    generate_pages_recursive,
    generate_page,
)
from copy_source import (
    clear_destination_and_copy_to,
)

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        print(basepath)
    source = "./static"
    destination = "./docs"
    clear_destination_and_copy_to(source, destination)
    generate_pages_recursive("content/", "template.html", destination, basepath)


if __name__ == "__main__":
    main()