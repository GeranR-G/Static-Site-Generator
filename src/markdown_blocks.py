from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block == "":
            continue
        new_blocks.append(block.strip())
    return new_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_nodes.append(block_to_html_node(block))
    return ParentNode("div", html_nodes)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block) 
    raise ValueError("Invalid markdown: Unknown block type")

def block_to_block_type(block):
    block_lines = block.split("\n")
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
        ):
        return block_type_heading
    if len(block_lines) > 1 and block_lines[0].startswith("```") and block_lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in block_lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in block_lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in block_lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        for i in range(len(block_lines)):
            if not block_lines[i].startswith(f"{i+1}. "):
                return block_type_paragraph
        return block_type_olist
    return block_type_paragraph

def text_to_nodes(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
         children.append(text_node_to_html_node(node))
    return children

def paragraph_to_html_node(block):
    return ParentNode("p", text_to_nodes(" ".join(block.split("\n"))))

def heading_to_html_node(block):
    heading = 0
    for char in block:
        if char == "#":
            heading += 1
        else:
            break
    if heading + 1 >= len(block):
        raise ValueError(f"Invalid headling level: {heading}")
    return ParentNode(f"h{heading}", text_to_nodes(block[heading + 1 :]))
    
def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    return ParentNode("pre", [ParentNode("code", text_to_nodes(block[3:-3]))])

def quote_to_html_node(block):
    block_lines = block.split("\n")
    stripped_lines = []
    for line in block_lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        stripped_lines.append(line.lstrip(">").strip())
    return ParentNode("blockquote", text_to_nodes(" ".join(stripped_lines)))

def ulist_to_html_node(block):
    block_lines = block.split("\n")
    node_list = []
    for line in block_lines:
        node_list.append(ParentNode("li", text_to_nodes(line[2:])))
    return ParentNode("ul", node_list)

def olist_to_html_node(block):
    block_lines = block.split("\n")
    node_list = []
    for line in block_lines:
        node_list.append(ParentNode("li", text_to_nodes(line[3:])))
    return ParentNode("ol", node_list)