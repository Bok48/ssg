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
        children.append(block_to_html_node(block))
        # Create HTMLNode with proper data based on type

        # Assign proper child (HTMLNode) objects to the block node

        # Code block should not do any inline markdown parsing of children
        # add child node to children list
    # Make all block nodes children under a single parent HTMLNode (div) and return
    parent_node = ParentNode("div", children)
    return parent_node

# Takes markdown block, returns new HTMLNode with the data
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            children = []
            text = block.replace('\n', ' ')
            textnodes = text_to_textnodes(text)
            for textnode in textnodes:
                children.append(text_node_to_html_node(textnode))
            htmlnode = ParentNode('p', children)
            return htmlnode
        #case BlockType.HEADING:
        case BlockType.CODE:
            htmlnode = code_block_to_html_node(block)
            return htmlnode
        #case BlockType.QUOTE:
        #case BlockType.UNORDERED_LIST:
        #case BlockType.ORDERED_LIST:
    return children

## Helper functions for block_to_html_node
def code_block_to_html_node(block):
    block = block.strip("`")
    block = block.lstrip('\n')
    textnode = TextNode(block, TextType.CODE)
    codenode = text_node_to_html_node(textnode) # LeafNode with code text
    htmlnode = ParentNode("pre", [codenode]) # ParentNode with code node as child and pre tag for html
    return htmlnode