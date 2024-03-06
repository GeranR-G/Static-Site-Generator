import os, shutil
from copystatic import copy_directory

origin_path = "./static/"
destination_path = "./public/"

def main():
    if os.path.exists(destination_path):
        print("Deleting public directory...")
        shutil.rmtree(destination_path)
    print("Copying static files to public directory...")
    copy_directory(origin_path, destination_path)

main()