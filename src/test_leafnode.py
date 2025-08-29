import unittest

from htmlnode import LeafNode

class TestLeaftNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_value_error(self):
        node = LeafNode(None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
