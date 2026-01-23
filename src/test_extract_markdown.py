import unittest

from extract_markdown import (
    extract_title,
)

class TextExtractMarkdown(unittest.TestCase):

    def test_simple_header(self):
        md = """
# Main title
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Main title"
        )

    def test_header(self):
        md = """
# Valid title

## Subtitle
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Valid title"
        )

    def test_header_2(self):
        md = """
Something written

# Only title

Something else
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Only title"
        )