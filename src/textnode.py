from enum import Enum

class NodeType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type: NodeType, url=None):
        if not isinstance(text_type, NodeType):
            raise ValueError(f"text_type must be an instance of NodeType, got {type(text_type)}")
        self.text = text
        self.type = text_type
        self.url = url

    def __eq__(self, value):
        return {self.text, self.type, self.url} == {value.text, value.type, value.url}

    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"