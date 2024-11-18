from src.htmlnode import LeafNode
from src.lib.text_type import TextType

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT.value:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD.value:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC.value:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE.value:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK.value:
        return LeafNode("a", text_node.text, {"href":text_node.url })
    elif text_node.text_type == TextType.IMAGE.value:
        return LeafNode("img", "", {"src":text_node.url, "alt": text_node.text })
    else:
        raise Exception("Invalid TextNode: no text type")