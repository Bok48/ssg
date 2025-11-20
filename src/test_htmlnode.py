import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # htmlnode
    def test_htmlnode(self):
        node = HTMLNode("a", "Link text", None, {"href": "http://localhost:8888", "target": "_blank"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Link text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "http://localhost:8888", "target": "_blank"})

    def test_htmlnode_2(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_htmlnode_3(self):
        list_nodes = []
        list_nodes.append(HTMLNode("li", "Item 1"))
        list_nodes.append(HTMLNode("li", "Item 2"))
        list_nodes.append(HTMLNode("li", "Item 3"))
        list_nodes.append(HTMLNode("li", "Item 4"))
        node = HTMLNode("ul", None, list_nodes)

        self.assertEqual(node.tag, "ul")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children[0], HTMLNode("li", "Item 1"))
        self.assertEqual(node.children[3], HTMLNode("li", "Item 4"))
        self.assertEqual(node.props, None)

    # eq
    def test_eq(self):
        node = HTMLNode("a", "Link text", None, {"href": "http://localhost:8888", "target": "_blank"})
        node2 = HTMLNode("a", "Link text", None, {"href": "http://localhost:8888", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = HTMLNode("a", "Link text", None, {"href": "http://localhost:8888", "target": "_blank"})
        node2 = HTMLNode("a", "Other link text", None, {"href": "http://localhost:8888", "target": "_blank"})
        self.assertNotEqual(node, node2)
  
    # repr
    def test_repr(self):
        node = HTMLNode("a", "Link text", None, {"href": "http://localhost:8888", "target": "_blank"})
        node_string = "HTMLNode(a, Link text, None, {'href': 'http://localhost:8888', 'target': '_blank'})"
        self.assertEqual(repr(node), node_string)


if __name__ == "__main__":
    unittest.main()