import unittest

from htmlnode import HTMLNode

TEST_PROPS = {
    "href": "https://www.google.com",
    "target": "_blank",
}

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="link", props=TEST_PROPS)
        self.assertEqual(node.props_to_html(),  'href="https://www.google.com" target="_blank"')
    
    def test_repr(self):
        node = HTMLNode()
        self.assertEqual(str(node), "HTMLNode(None, None, None, None)")
    
    def test_repr_with_props(self):
        node = HTMLNode(tag="href", props=TEST_PROPS)
        self.assertEqual(str(node), f"HTMLNode(href, None, None, {TEST_PROPS})")





if __name__ == "__main__":
    unittest.main()
