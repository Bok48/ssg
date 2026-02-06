from generate_page import(
    generate_pages_recursive,
    generate_page,
)
from copy_source import (
    clear_destination_and_copy_to,
)

def main():
    source = "./static"
    destination = "./public"
    clear_destination_and_copy_to(source, destination)
    generate_pages_recursive("content/", "template.html", "public/")


if __name__ == "__main__":
    main()