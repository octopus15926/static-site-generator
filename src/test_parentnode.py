import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode(tag="span", value="child")
        parent_node = ParentNode(children=[child_node], tag="div")
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode(tag="b", value="grandchild")
        child_node = ParentNode(children=[grandchild_node], tag="span")
        parent_node = ParentNode(children=[child_node], tag="div")
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
