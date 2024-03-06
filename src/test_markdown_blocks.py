import unittest
from markdown_blocks import(
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    block_to_html_node,
    paragraph_to_html_node,
    heading_to_html_node,
    code_to_html_node,
    quote_to_html_node,
    ulist_to_html_node,
    olist_to_html_node,
)

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
            blocks,
        )

    def test_markdown_to_blocks_newlines(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        ) 

    def test_block_to_block_type_heading(self):
        block_list = [
            "# Heading 1",
            "## Heading 2",
            "### Heading 3",
            "#### Heading 4",
            "##### Heading 5",
            "###### Heading 6",
        ]
        block_type_list = []
        for block in block_list:
            block_type_list.append(block_to_block_type(block))
        self.assertListEqual(
            [
                "heading",
                "heading",
                "heading",
                "heading",
                "heading",
                "heading",
            ],
            block_type_list,
        )

    def test_block_to_block_type_code_block(self):
        code_block = "```\nThis isn't even code\n```"
        block_type = block_to_block_type(code_block)
        self.assertEqual(
            "code",
            block_type,
        )

    def test_block_to_block_type_quote(self):
        quote = ">I am not\n>actually\n>quoting anything"
        block_type = block_to_block_type(quote)
        self.assertEqual(
            "quote",
            block_type
        )
    
    def test_block_to_block_type_unordered_list(self):
        list = "* This is\n* not\n* an ordered\n* list"
        block_type = block_to_block_type(list)
        self.assertEqual(
            "unordered_list",
            block_type
        )

    def test_block_to_block_type_unordered_list(self):
        list = "- This is\n- also not\n- an ordered\n- list"
        block_type = block_to_block_type(list)
        self.assertEqual(
            "unordered_list",
            block_type
        )

    def test_block_to_block_type_ordered_list(self):
        list = "1. This is\n2. an ordered list"
        block_type = block_to_block_type(list)
        self.assertEqual(
            "ordered_list",
            block_type
        )
    
    def test_paragraph_to_html_node(self):
        block = "This is a paragraph"
        node = paragraph_to_html_node(block)
        self.assertEqual(
            node.to_html(),
            "<p>This is a paragraph</p>"
        )

    def test_heading_to_html_node(self):
        block = "### This is a heading"
        node = heading_to_html_node(block)
        self.assertEqual(
            node.to_html(),
            "<h3>This is a heading</h3>"
        )

    def test_code_to_html_node(self):
        block = "```This isn't\neven code```"
        node = code_to_html_node(block)
        self.assertEqual(
            node.to_html(),
            "<pre><code>This isn't\neven code</code></pre>"
        )

    def test_quote_to_html_node(self):
        block = ">I am not\n>even quoting\n>anything"
        node = quote_to_html_node(block)
        self.assertEqual(
            node.to_html(),
            "<blockquote>I am not even quoting anything</blockquote>"
        )

    def test_ulist_to_html_node(self):
        block = "* this is an\n* unordered list"
        node = ulist_to_html_node(block)
        self.assertEqual(
            node.to_html(),
            "<ul><li>this is an</li><li>unordered list</li></ul>"
        )
    
    def test_olist_to_html_node(self):
        block = "1. this is an\n2. ordered list"
        node = olist_to_html_node(block)
        self.assertEqual(
            node.to_html(),
            "<ol><li>this is an</li><li>ordered list</li></ol>"
        )

    def test_block_to_html_node(self):
        block = "- this is an\n- unordered list"
        node = block_to_html_node(block)
        self.assertEqual(
            node.to_html(),
            "<ul><li>this is an</li><li>unordered list</li></ul>"
        )

    def test_markdown_to_html_node(self):
        markdown = """
# This is a **bolded** heading

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><h1>This is a <b>bolded</b> heading</h1><p>This is another paragraph with <i>italic</i> text and <code>code</code> here This is the same paragraph on a new line</p><ul><li>This is a list</li><li>with items</li></ul></div>"
        )

if __name__ == "__main__":
    unittest.main()