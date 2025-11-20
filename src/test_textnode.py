import unittest

from textnode import TextType, TextNode


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


if __name__ == "__main__":
    unittest.main()