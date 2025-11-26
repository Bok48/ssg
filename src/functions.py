def markdown_to_blocks(markdown):
    markdown_blocks = markdown.split("\n\n")
    markdown_blocks = [markdown.strip(' \n') for markdown in markdown_blocks if markdown != ""]
    return markdown_blocks