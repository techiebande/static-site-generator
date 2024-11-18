from src.utils.text_node_to_html_node import text_node_to_html_node
from src.lib.text_type import TextType


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

    

# text_node = TextNode("Obande", TextType.BOLD).text
# print(text_node)
# print(text_node_to_html_node(text_node).to_html())