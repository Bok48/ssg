from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    markdown_blocks = markdown.split("\n\n")
    markdown_blocks = [markdown.strip(' \n') for markdown in markdown_blocks if markdown != ""]
    return markdown_blocks

# Takes single block of markdown text, returns the type of block (BlockType).
# It is assumed that the block does not have leading and trailing whitespace.
def block_to_block_type(block):
    if block is None:
        raise Exception("No block given to the function")
    if len(block) == 0:
        raise Exception("Empty block given to the function")

    match block[0]:
        case '#': # May be a header
            header = block.split(' ')[0]
            if header.count('#') == len(header):
                return BlockType.HEADING
        case '`': # May be a code block
            if len(block) > 6 and block[:3] == "```" and block[-3:] == "```":
                return BlockType.CODE
        case '>': # May be a quote block
            lines = block.split('\n')
            are_quotes = True
            for line in lines:
                if line != "" and line[0] != '>':
                    are_quotes = False
            if are_quotes:
                return BlockType.QUOTE
        case '-': # May be an unordered list
            lines = block.split('\n')
            is_list = True
            for line in lines:
                if line != "" and line[:2] != "- ":
                    is_list = False
            if is_list:
                return BlockType.UNORDERED_LIST
        case '1': # May be an ordered list
            lines = block.split('\n')
            is_list = True
            for line in lines:
                if line != "" and line[1:3] != ". ":
                    is_list = False
            if is_list:
                return BlockType.ORDERED_LIST
        
    return BlockType.PARAGRAPH # Default BlockType if no other match