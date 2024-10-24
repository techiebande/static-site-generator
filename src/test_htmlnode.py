import unittest

from htmlnode import HTMLNode

class TextHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(tag="div", children=[
            HTMLNode(tag="p", value="I am a paragraph", children=[], props={
                "class": "text-red-500"
            })
        ], props={
            "class": "flex items-center justify-between"
        })

        self.assertEqual(node.props_to_html(), ' class="flex items-center justify-between"')

        self.assertNotEqual(node.props_to_html(), 'class="flex items-center justify-between"')

        self.assertNotEqual(node.props_to_html(), ' class="flex items-center justify-between "')



if __name__ == "__main__":
    unittest.main()