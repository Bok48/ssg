from enum import Enum
import re

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            link_dict = {'href': text_node.url}
            return LeafNode("a", text_node.text, link_dict)
        case TextType.IMAGE:
            image_dict = {'src': text_node.url, 'alt': text_node.text}
            return LeafNode("img", None, image_dict)
        case _:
            raise ValueError(f"Text type {text_node.text_type.value} is not usable")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        opening_delimiter = False
        delimiter_index = 0 # The index *after* a delimiter
        delimiter_len = len(delimiter)
        for char_index in range(len(node.text)):
            if node.text[char_index:char_index + delimiter_len] == delimiter:
                if opening_delimiter: # If an opening delimiter has been passed
                    if delimiter_index < char_index:
                        new_nodes.append(
                            TextNode(node.text[delimiter_index:char_index], text_type)
                        )
                    opening_delimiter = False
                else:
                    if delimiter_index < char_index:
                        new_nodes.append(
                            TextNode(node.text[delimiter_index:char_index], TextType.TEXT)
                        )
                    opening_delimiter = True
                delimiter_index = char_index + delimiter_len
        if opening_delimiter:
            raise Exception(f"Could not find closing delimiter for text type {text_type.value} (delimiter: {delimiter})")

        if delimiter_index < len(node.text):
            new_nodes.append(
                TextNode(node.text[delimiter_index:], TextType.TEXT)
            )

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text) # find parts of string matching "![...](...)"

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text) # find parts of string matching "[...](...) without preceding '!'"


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_strings = re.split(r"(!\[.*?\]\(.*?\))", node.text)
        for i in range(len(node_strings)):
            if node_strings[i] == "":
                continue
            if i % 2 == 1:
                extracted_image = extract_markdown_images(node_strings[i])
                new_nodes.append(
                    TextNode(extracted_image[0][0], TextType.IMAGE, extracted_image[0][1])
                )
            else:
                new_nodes.append(
                    TextNode(node_strings[i], TextType.TEXT)
                )
    return new_nodes
                

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_strings = re.split(r"((?<!!)\[.*?\]\(.*?\))", node.text)
        for i in range(len(node_strings)):
            if node_strings[i] == "":
                continue
            if i % 2 == 1:
                extracted_image = extract_markdown_links(node_strings[i])
                new_nodes.append(
                    TextNode(extracted_image[0][0], TextType.LINK, extracted_image[0][1])
                )
            else:
                new_nodes.append(
                    TextNode(node_strings[i], TextType.TEXT)
                )
    return new_nodes