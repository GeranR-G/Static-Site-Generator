import os, shutil

def copy_directory(origin_directory, destination_directory):
    if not os.path.exists(origin_directory):
        raise ValueError("Invalid origin directory path")
    if not os.path.exists(destination_directory):
        os.mkdir(destination_directory)
    for dir in os.listdir(origin_directory):
        destination_path = os.path.join(destination_directory, dir)
        origin_path = os.path.join(origin_directory, dir)
        if os.path.isfile(origin_path):
            print(f"File origin path: {origin_path}. File destination path: {destination_path}")
            shutil.copy(origin_path, destination_path)
        else:
            copy_directory(origin_path, destination_path)