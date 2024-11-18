import unittest
from src.textnode import TextNode
from src.lib.text_type import TextType
from src.utils.split_nodes_delimeter import split_nodes_delimiter

class Test_Split_Nodes_Delimiter(unittest.TestCase):
    def test_no_delimiter(self):
        old_node = TextNode("this is a text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "`", TextType.CODE)

        self.assertEqual(old_node, new_nodes[0])
    
    def test_with_delimiter(self):
        old_node = TextNode("this is a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1], TextNode('code block', TextType.CODE, None))
    
    def test_two_nodes(self):
        old_node1 = TextNode("this is a normal text", TextType.TEXT)
        old_node2 = TextNode("this is a `code block` word", TextType.TEXT)

        new_nodes = split_nodes_delimiter([old_node1, old_node2], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[2], TextNode('code block', TextType.CODE, None))

    def test_no_closing_delimiter(self):
        old_node = TextNode("this is a `code block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([old_node], "`", TextType.CODE)

    def test_code_blocks(self):
        old_node = TextNode("this is a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "`", TextType.CODE)

        self.assertEqual(new_nodes[1], TextNode('code block', TextType.CODE, None))

    def test_italics(self):
        old_node = TextNode("this is an *italic* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "*", TextType.ITALIC)

        self.assertEqual(new_nodes[1], TextNode('italic', TextType.ITALIC, None))

    def test_bold_txt(self):
        old_node = TextNode("this is an **bolded** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)

        self.assertEqual(new_nodes[1], TextNode('bolded', TextType.BOLD, None))


if __name__ == "__main__":
    unittest.main()