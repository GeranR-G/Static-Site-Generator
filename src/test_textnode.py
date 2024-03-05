import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_neq(self):
            node = TextNode("This is a text node", text_type_text)
            node2 = TextNode("This is also a text node", text_type_text)
            self.assertNotEqual(node,node2)

    def test_url_None(self):
            node = TextNode("This is a text node", text_type_text)
            node2 = TextNode("This is a text node", text_type_text, None)
            self.assertEqual(node,node2)

    def test_text_type_neq(self):
            node = TextNode("This is a text node", text_type_bold)
            node2 = TextNode("This is a text node", text_type_text)
            self.assertNotEqual(node,node2)

    def test_url_neq(self):
            node = TextNode("This is a text node", text_type_text)
            node2 = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
            self.assertNotEqual(node,node2)

    def test_eq_url(self):
            node = TextNode("This is a text node", text_type_text,"https://www.boot.dev")
            node2 = TextNode(
                   "This is a text node", text_type_text, "https://www.boot.dev"
                   )
            self.assertEqual(node,node2)

    def  test_repr(self):
            node = TextNode("This is a text node", text_type_text,"https://www.boot.dev")
            self.assertEqual(
                   "TextNode(This is a text node, text, https://www.boot.dev)",repr(node)
                   )

if __name__ == "__main__":
    unittest.main()
