import unittest

from textnode import TextNode, NodeType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("obande", NodeType.NORMAL)
        node2 = TextNode("obande", NodeType.NORMAL)

        node3 = TextNode("obande is my name", NodeType.NORMAL, "https://google.com")
        node4 = TextNode("obande is my name", NodeType.NORMAL, "https://google.com")

        self.assertEqual(node1, node2)
        self.assertEqual(node3, node4)
    
    def test_not_equal(self):
        node1 = TextNode("obande", NodeType.BOLD)
        node2 = TextNode("obande", NodeType.NORMAL)

        self.assertNotEqual(node1, node2)
    
    def test_string_representation(self):
        node = TextNode("obande", NodeType.NORMAL)

        self.assertEqual("TextNode(obande, normal, None)", str(node))
    
    def test_None(self):
        node = TextNode("obande", NodeType.BOLD)

        self.assertEqual("TextNode(obande, bold, None)", str(node))



if __name__ == "__main__":
    unittest.main()