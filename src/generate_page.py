import os
from markdown_blocks import(
     markdown_to_blocks,
     markdown_to_html_node
)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    title = None
    for block in blocks:
        if "# " in block:
            if title == None:
                title = block.lsplit("# ").split()
            else:
                raise ValueError("Invalid markdown: multiple h1 headers")
    if title == None:
        raise ValueError("Invalid markdown: missing h1 header")
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}, using {template_path}")
    f = open(from_path)
    markdown = f.read()
    f.close()
    f = open(template_path)
    template = f.read()
    f.close()
    markdown_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template.replace("{{ Title }}", title)
    template.replace("{{ Content }}", markdown_html)
    dest_path_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_path_dir):
        os.makedirs(dest_path_dir)
    new_HTML = open(dest_path, "w")
    new_HTML.write(template)
    new_HTML.close()