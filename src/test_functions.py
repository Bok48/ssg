import unittest
from functions import (
    markdown_to_blocks,
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
