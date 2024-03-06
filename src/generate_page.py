import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for dir in os.listdir(dir_path_content):
        origin_path = os.path.join(dir_path_content, dir)
        destination_path = os.path.join(dest_dir_path, dir)
        if os.path.isfile(origin_path):
            destination_path = Path(destination_path).with_suffix(".html")
            generate_page(origin_path, template_path, destination_path)
        else:
            generate_pages_recursive(origin_path, template_path, destination_path)

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
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", markdown_html)

    dest_path_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_path_dir):
        os.makedirs(dest_path_dir)
    new_HTML = open(dest_path, "w")
    new_HTML.write(template)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("Invalid markdown: missing h1 header")