import unittest
from functions import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
)

class TestFunctions(unittest.TestCase):

    # markdown_to_blocks
    def test_markdown_to_blocks(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        result = markdown_to_blocks(md)
        expected_result = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ]

    def test_markdown_spaces(self):
        md = """
    This is markdown with three leading spaces.

This is markdown with three trailing spaces.    
"""
        result = markdown_to_blocks(md)
        expected_result = [
            "This is markdown with three leading spaces.",
            "This is markdown with three trailing spaces.",
        ]
        self.assertEqual(result, expected_result)

    def test_markdown_newlines(self):
        md = """
\n
This text has a lot of\n
\nnewlines included
\n\n
\n
Some other text

"""
        result = markdown_to_blocks(md)
        expected_result = [
            "This text has a lot of",
            "newlines included",
            "Some other text",
        ]
        self.assertEqual(result, expected_result)

    
    # block_to_block_type
    def test_block_to_paragraph(self):
        block = "This is a paragraph of text in markdown"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_block_to_heading(self):
        block = "## This is a h2 heading in markdown"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_block_to_code(self):
        block = "```This is a block of code in markdown```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_block_to_quote(self):
        block = """>This is a quote block in markdown.
>Every line starts with a '>' symbol.
"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)
    
    def test_block_to_unordered_list(self):
        block = """- This is an unordered list.
- Every line must start with a '-' symbol followed by a space.        
"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)
    
    def test_block_to_ordered_list(self):
        block = """1. This is an ordered list.
2. Every line must start with a number, followed by a '.' and a space.
"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

