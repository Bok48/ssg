from enum import Enum

from textnode import (
    TextType,
    TextNode,
    text_to_textnodes,
    text_node_to_html_node,
)
from htmlnode import (
    ParentNode,
    LeafNode,
)

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
            if len(header) < 7 and header.count('#') == len(header):
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

# Takes a full markdown document and converts it to a single parent HTMLNode
# with relevant child nodes nested inside.
def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    children = []
    for block in md_blocks:
        # Create and append HTMLNode with proper data based on type
        children.append(block_to_html_node(block))
    parent_node = ParentNode("div", children)
    return parent_node

# Takes markdown block, returns new HTMLNode with the data
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_block_to_html_node(block)
        case BlockType.HEADING:
            return heading_block_to_html_node(block)
        case BlockType.CODE:
            return code_block_to_html_node(block)
        case BlockType.QUOTE:
            return  quote_block_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_block_to_html_node(block) 
        case BlockType.ORDERED_LIST:
            return ordered_list_block_to_html_node(block)
    return children

## Helper functions for block_to_html_node
## Takes one block and creates a relevant html node
def paragraph_block_to_html_node(block):
    children = []
    text = block.replace('\n', ' ')
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    htmlnode = ParentNode('p', children)
    return htmlnode

def heading_block_to_html_node(block):
    children = []
    content = block.split(' ', 1)
    header_count = content[0].count('#')
    textnodes = text_to_textnodes(content[1])
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    htmlnode = ParentNode(f"h{header_count}", children)
    return htmlnode

def code_block_to_html_node(block):
    block = block.strip("`")
    block = block.lstrip('\n')
    textnode = TextNode(block, TextType.CODE)
    codenode = text_node_to_html_node(textnode) # LeafNode with code text
    htmlnode = ParentNode("pre", [codenode]) # ParentNode with code node as child and pre tag for html
    return htmlnode

def quote_block_to_html_node(block):
    children = []
    lines = block.split('\n')
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line[2:]) # Line without "> " in front
    lines = ' '.join(cleaned_lines)
    textnodes = text_to_textnodes(lines)
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    htmlnode = ParentNode('q', children)
    return htmlnode

def unordered_list_block_to_html_node(block):
    children = []
    lines = block.split('\n')
    for line in lines:
        cleaned_line = line[2:] # Line without "- " in front
        textnodes = text_to_textnodes(cleaned_line)
        li_children = []
        for textnode in textnodes:
            li_children.append(text_node_to_html_node(textnode))
        listnode = ParentNode("li", li_children)
        children.append(listnode)
    htmlnode = ParentNode("ul", children)
    return htmlnode

def ordered_list_block_to_html_node(block):
    children = []
    lines = block.split('\n')
    for line in lines:
        cleaned_line = line[3:] # Line without "1. ", "2. " in front
        textnodes = text_to_textnodes(cleaned_line)
        li_children = []
        for textnode in textnodes:
            li_children.append(text_node_to_html_node(textnode))
        listnode = ParentNode("li", li_children)
        children.append(listnode)
    htmlnode = ParentNode("ol", children)
    return htmlnode
