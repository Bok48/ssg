import unittest
from functions import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
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

    # markdown_to_html_node
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""   
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_heading(self):
        md = """
### This is an h3 header that should be inside a h3 tag
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is an h3 header that should be inside a h3 tag</h3></div>"
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quotes(self):
        md = """
> This is **bolded** quote
> text in a q
> tag here

> This is another quote with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><q>This is <b>bolded</b> quote text in a q tag here</q><q>This is another quote with <i>italic</i> text and <code>code</code> here</q></div>",
        )

    def test_unordered_list(self):
        md = """
- This is an unordered list
- Every line here
- Should be its own list item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an unordered list</li><li>Every line here</li><li>Should be its own list item</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. This is an ordered list
2. Every line here
3. Should be its own list item
4. In the right order
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an ordered list</li><li>Every line here</li><li>Should be its own list item</li><li>In the right order</li></ol></div>"
        )