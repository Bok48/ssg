import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        node_text = "TextNode(This is a text node, bold, None)"
        self.assertEqual(str(node), node_text)



if __name__ == "__main__":
    unittest.main()