import unittest
from extract_markdown_links import extract_markdown_links


class Test_Extract_Markdown_Links(unittest.TestCase):
    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)

        self.assertEqual(2, len(result))
        self.assertEqual("to boot dev", result[0][0])
        self.assertEqual("https://www.boot.dev", result[0][1])

        self.assertEqual("to youtube", result[1][0])
        self.assertEqual("https://www.youtube.com/@bootdotdev", result[1][1])

