from enum import Enum

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        prop_keys = self.props.keys()
        prop_string = ""
        for key in prop_keys:
            prop_string += f'{key}="{self.props[key]}" '
        return prop_string.rstrip()

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        return f'<{self.tag}{f" {self.props_to_html()}" if self.props else ""}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, value=None, props=None):
        super().__init__(tag=tag, children=children, value=value, props=props)


    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNodes must have a tag!")
        if not self.children:
            raise ValueError("ParentNodes must have children!")
        html_output = f"<{self.tag}>"
        for child in self.children:
            html_output += child.to_html()
        html_output += f"</{self.tag}>"
        return html_output

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_text_node):
        if self.text == other_text_node.text and self.text_type == other_text_node.text_type and self.url == other_text_node.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.url, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"{text_node.text_type} is not a valid TextType!")


