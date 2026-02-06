import os
from functions import (
    markdown_to_html_node,
    markdown_to_blocks,
)
from extract_markdown import (
    extract_title,
)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    source_dir_contents = os.listdir(dir_path_content)
    for item in source_dir_contents:
        source_item_path = os.path.join(dir_path_content, item)
        dest_item_path = os.path.join(dest_dir_path, item)
        if os.path.isdir(source_item_path):
            os.mkdir(dest_item_path)
            generate_pages_recursive(source_item_path, template_path, dest_item_path, basepath)
        else:
            filepath, extension = os.path.splitext(dest_item_path)
            if extension == ".md":
                dest_item_path = f"{filepath}.html"
            generate_page(source_item_path, template_path, dest_item_path, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
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
    template_file_contents = template_file_contents.replace('href="/', f'href="{basepath}')
    template_file_contents = template_file_contents.replace('src="/', f'src="{basepath}')
    current_dest_path = os.path.dirname(dest_path)
    if not os.path.exists(current_dest_path):
        os.makedirs(current_dest_path)
    with open(dest_path, 'w') as f:
        f.write(template_file_contents)
    print(f"Generated_file: {dest_path}")