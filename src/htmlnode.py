

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # string representing tag name ("a", "h1")
        self.value = value # string representing the contents, e.g. paragraph text
        self.children = children # list of HTMLNode objects
        self.props = props # dicionary of tag attributes

    def to_html(self):
        raise NotImplementedError("HTMLNode method to_html() not implemented")

    def props_to_html(self):
        props_string = ""
        if self.props is not None and len(self.props) != 0:
            for key in self.props:
                props_string += f' {key}="{self.props[key]}"'
        return props_string
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'