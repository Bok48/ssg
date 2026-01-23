from functions import (
    markdown_to_blocks,
)

def extract_title(markdown):
    md_blocks = markdown_to_blocks(markdown)
    for block in md_blocks:
        line_split = block.split(' ', 1)
        if len(line_split[0]) == 1 and line_split[0] == "#" and len(line_split) > 1 and len(line_split[1]) < 60:
            return line_split[1]
    raise Exception("Error: valid markdown h1 header not found. Make sure main header starts with a single '#'")
