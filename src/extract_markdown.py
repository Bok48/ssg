import os

from functions import (
    markdown_to_html_node,
    markdown_to_blocks,
)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    #if not os.path.exists(from_path) or not os.path.exists(template_path):
    #    raise Exception(f"Error: file '{from_path}' was not found")
    source_file_contents = ""
    template_file_contents = ""
    with open(from_path) as f:
        source_file_contents = f.read()
    with open(template_path) as f:
        template_file_contents = f.read()
    html_node = markdown_to_html_node(source_file_contents)
    file_title = extract_title(source_file_contents)
    template_file_contents = template_file_contents.replace("{{ Title }}", file_title)
    template_file_contents = template_file_contents.replace("{{ Content }}", source_file_contents)
    print(f"Generated_file: {template_file_contents}")
    os.makedirs(dest_path)
    with open(dest_path, 'w') as f:
        f.write(template_file_contents)
        print(f"Page {dest_path} generated")

    


def extract_title(markdown):
    md_blocks = markdown_to_blocks(markdown)
    for block in md_blocks:
        line_split = block.split(' ', 1)
        if len(line_split[0]) == 1 and line_split[0] == "#" and len(line_split) > 1 and len(line_split[1]) < 60:
            return line_split[1]
    raise Exception("Error: valid markdown h1 header not found. Make sure main header starts with a single '#'")
