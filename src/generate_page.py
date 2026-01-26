import os
from functions import (
    markdown_to_html_node,
    markdown_to_blocks,
)
from extract_markdown import (
    extract_title,
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
    html_string = html_node.to_html()
    file_title = extract_title(source_file_contents)
    template_file_contents = template_file_contents.replace("{{ Title }}", file_title)
    template_file_contents = template_file_contents.replace("{{ Content }}", html_string)
    current_dest_path = os.path.dirname(dest_path)
    if not os.path.exists(current_dest_path):
        os.makedirs(current_dest_path)
    with open(dest_path, 'w') as f:
        f.write(template_file_contents)
    print(f"Generated_file: {dest_path}")