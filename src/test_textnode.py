import unittest

from textnode import (
    TextType,
    TextNode,
    text_node_to_html_node,
    split_nodes_delimiter,
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

    
    # split_nodes_delimiter
    def test_split_delimiter_from_bold(self):
        node = TextNode("This is bold text.", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is bold text.", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_delimiter_bold_start(self):
        node = TextNode("**This** is text with a bold word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This", TextType.BOLD),
            TextNode(" is text with a bold word.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)
        

    def test_split_delimiter_italic_end(self):
        node = TextNode("This is text with _italic text._", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("italic text.", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_delimiter_code_full_text(self):
        node = TextNode("```This is all code```", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "```", TextType.CODE)
        expected_nodes = [
            TextNode("This is all code", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_delimiter_node_list(self):
        nodes = [
            TextNode("This is text with _italic_ text.", TextType.TEXT),
            TextNode("Bold text", TextType.BOLD),
            TextNode("This is _italic text._", TextType.TEXT),
            TextNode("This is normal text", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
            TextNode("Bold text", TextType.BOLD),
            TextNode("This is ", TextType.TEXT),
            TextNode("italic text.", TextType.ITALIC),
            TextNode("This is normal text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)


        


if __name__ == "__main__":
    unittest.main()