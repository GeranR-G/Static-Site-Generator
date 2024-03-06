import os, shutil
from copystatic import copy_directory
from generate_page import generate_page

static_path = "./static/"
destination_path = "./public/"
index_path = "./content/index.md"
template_path = "./template.html"


def main():
    if os.path.exists(destination_path):
        print("Deleting public directory...")
        shutil.rmtree(destination_path)
    print("Copying static files to public directory...")
    copy_directory(static_path, destination_path)
    generate_page(index_path, template_path, destination_path+"index.html")

main()