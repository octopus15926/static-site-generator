from htmlnode import HTMLNode

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

