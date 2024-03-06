import os, shutil
from copystatic import copy_directory
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if os.path.exists(dir_path_public):
        print("Deleting public directory...")
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_directory(dir_path_static, dir_path_public)
    
    print("Generating page...")
    generate_pages_recursive(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html")
    )

main()