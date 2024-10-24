from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, **kwargs):
        if "children" in kwargs:
            raise ValueError("A leaf node should not have children")
        
        super().__init__(value=value, **kwargs)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return self.value
        else:
            return f'''<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'''

# leaf_node = LeafNode(tag="p", value="")
# leaf_node2 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})

# print(leaf_node.to_html())
# print(leaf_node2.to_html())
