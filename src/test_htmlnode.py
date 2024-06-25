import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Test 1
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        expected_result =  ' href="https://www.google.com" target="_blank"'
        props_string = node.props_to_html()
        self.assertEqual(props_string, expected_result)

        # Test 2
        node = HTMLNode(None, None, None, {"a": "exampleA", "b": "exampleB", "foo": "bar"})
        expected_result = ' a="exampleA" b="exampleB" foo="bar"'
        props_string = node.props_to_html()
        self.assertEqual(props_string, expected_result)

    def test___repr__(self):
        node = HTMLNode("<p>", "This is example text", None, {"a": "exampleA", "b": "exampleB", "foo": "bar"})
        expected_result = "HTMLNode(tag: <p>, value: This is example text, children: None, props: {'a': 'exampleA', 'b': 'exampleB', 'foo': 'bar'})"
        self.assertEqual(str(node), expected_result)
        
        # node_list = [HTMLNode("<p>", "This is example text", None, {"a": "exampleA", "b": "exampleB", "foo": "bar"}),
        #              HTMLNode("<h1>", "This is header text", None, {"lol": "nah"})]
        # print(node_list)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        # Test 1
        node = LeafNode("p", "This is a paragraph of text.")
        result = node.to_html()
        expected_result = '<p>This is a paragraph of text.</p>'
        self.assertEqual(result, expected_result)

        # Test 2
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result2 = node2.to_html()
        expected_result2 = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(result2, expected_result2)

        # Test 3
        node3 = LeafNode(None, "Hello there!")
        result3 = node3.to_html()
        expected_result3 = "Hello there!"
        self.assertEqual(result3, expected_result3)


if __name__ == "__main__":
    unittest.main()
