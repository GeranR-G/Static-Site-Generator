import unittest
from markdown_blocks import(
    markdown_to_blocks,
    block_to_block_type
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

if __name__ == "__main__":
    unittest.main()