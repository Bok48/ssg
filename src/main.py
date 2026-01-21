
import os
import shutil

def main():
    clear_and_copy_to_destination()


def clear_and_copy_to_destination():
    source = "static"
    destination = "public"
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print("Public folder cleared")
    os.mkdir(destination)
    copy_dir_contents(source, destination)
    
def copy_dir_contents(source, destination):
    if not os.path.exists(source):
        raise Exception(f"Source folder {source} does not exist in the directory")
    
    for item in os.listdir(source):
        item_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dest_path)
            print(f"Copied file {item_path} to public folder")
        else:
            os.mkdir(dest_path)
            copy_dir_contents(item_path, dest_path)
        


if __name__ == "__main__":
    main()