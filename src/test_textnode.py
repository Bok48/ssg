import unittest

from textnode import (
    TextType,
    TextNode,
    text_node_to_html_node,
)


class TestTextNode(unittest.TestCase):
    # textnode
    def test_textnode(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type.value, "bold")
        self.assertEqual(node.url, None)

    def test_textnode_2(self):
        node = TextNode("", TextType.LINK, "https://localhost:8888")
        self.assertEqual(node.text, "")
        self.assertEqual(node.text_type.value, "link")
        self.assertEqual(node.url, "https://localhost:8888")

    def test_textnode_3(self):
        node = TextNode(None, None, None)
        self.assertEqual(node.text, None)
        self.assertEqual(node.text_type, None)
        self.assertEqual(node.url, None)

    # eq
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("These are two different text nodes", TextType.BOLD)
        node2 = TextNode("These are two different text nodes", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    # repr
    def test_repr(self):
        node = TextNode("This is a url", TextType.LINK, "http://localhost:8888")
        node_text = "TextNode(This is a url, link, http://localhost:8888)"
        self.assertEqual(f"{node}", node_text)

    def test_repr_2(self):
        node = TextNode("This is a url", TextType.LINK)
        node_text = "TextNode(This is a url, link, http://localhost:8888)"
        self.assertNotEqual(f"{node}", node_text)

    # text_node_to_html_node
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("print('This is a node with code')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('This is a node with code')")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "http://localhost:8888")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {'href': "http://localhost:8888"})
    
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "http://localhost:8888")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {'src': "http://localhost:8888", 'alt': "This is an image node"})
        


if __name__ == "__main__":
    unittest.main()