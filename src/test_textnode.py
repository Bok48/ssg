import unittest

from textnode import TextNode
from textnode import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        node_text = "TextNode(This is a text node, bold, None)"
        self.assertEqual(str(node), node_text)

    def test_text_node_to_html_node(self):
        # Test 1 (text)
        node = TextNode("Hello world!", "text")
        result = str(text_node_to_html_node(node))
        expected_result = 'LeafNode(tag: None, value: Hello world!, props: None)'
        self.assertEqual(result, expected_result)

        # Test 2 (bold)
        node = TextNode("Hello world!", "bold")
        result = str(text_node_to_html_node(node))
        expected_result = 'LeafNode(tag: b, value: Hello world!, props: None)'
        self.assertEqual(result, expected_result)

        # Test 3 (italic)
        node = TextNode("Hello world!", "italic")
        result = str(text_node_to_html_node(node))
        expected_result = 'LeafNode(tag: i, value: Hello world!, props: None)'
        self.assertEqual(result, expected_result)

        # Test 4 (code)
        node = TextNode("Hello world!", "code")
        result = str(text_node_to_html_node(node))
        expected_result = 'LeafNode(tag: code, value: Hello world!, props: None)'
        self.assertEqual(result, expected_result)

        # Test 5 (link)
        node = TextNode("Hello world!", "link", "www.example.com")
        result = str(text_node_to_html_node(node))
        expected_result = "LeafNode(tag: a, value: Hello world!, props: {'href': 'www.example.com'})"
        self.assertEqual(result, expected_result)

        # Test 6 (image)
        node = TextNode("Hello world!", "image", "www.example.com")
        result = str(text_node_to_html_node(node))
        expected_result = "LeafNode(tag: img, value: , props: {'src': 'www.example.com', 'alt': 'Hello world!'})"
        self.assertEqual(result, expected_result)



if __name__ == "__main__":
    unittest.main()