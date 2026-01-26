from extract_markdown import(
    generate_page,
)
from copy_source import (
    clear_destination_and_copy_to,
)

def main():
    source = "./static"
    destination = "./public"
    clear_destination_and_copy_to(source, destination)
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()