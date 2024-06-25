

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    # This:           {"href": "https://www.google.com", "target": "_blank"}
    # Should become:  ' href="https://www.google.com" target="_blank"'
    def props_to_html(self):
        html_string = ''
        for prop in self.props:
            html_string += f' {prop}="{self.props[prop]}"'
        return html_string
    
    
    def __repr__(self):
        return f'HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})'
    


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=""):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No value set for leaf node")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'