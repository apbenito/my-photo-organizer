import os
import shutil


def create_template():
    pass


###CREATE LIST FROM TXT FILE###
def photos_from_txt(txt_path, photos_list=[]):
    # open file and get the img names into a list
    with open(txt_path, "r") as f:
        for line in f:
            line = line.replace("\n", "").split("-")  # clean up data
            line = [int(x) for x in line]  # turn into numbers
            if len(line) > 1:
                line = range(
                    line[0], line[1] + 1
                )  # unpack lines with more than 1 photo
            for photo in line:
                photos_list.append("_MG_" + str(photo))  # add all photos to list
    return photos_list


###REMOVE PHOTOS FROM RAW###
def remove_raw(folder_path, photos_list):
    """
    folder_path should lead to the "raw" folder
    """
    subfolders_path = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    if subfolders_path:  # if there ARE subfolders
        for subfolder in subfolders_path:
            for photo in photos_list:
                try:
                    os.remove(
                        os.path.join(
                            subfolder,
                            f"{photo}{os.path.basename(os.path.normpath(subfolder))}",
                        )
                    )
                    print(
                        f"Deleted {photo}{os.path.basename(os.path.normpath(subfolder))}"
                    )
                except FileNotFoundError:
                    print(
                        f"File {photo}{os.path.basename(os.path.normpath(subfolder))} was already deleted!"
                    )
    else:  # if there ARE NOT any subfolders:
        extension = input("What is the extension of the photos? (examples: .jpg, .png)")
        for photo in photos_list:
            try:
                os.remove(os.path.join(raw_photos_path, f"{photo}{extension}"))
                print(f"Deleted {f}{extension}")
            except FileNotFoundError:
                print(f"File {f}{extension} was already deleted!")

def move_selected(source_folder_path,destination_folder_path,photos_list):
    pass
if __name__ == "__main__":
    # parent_folder = input("Path of the folder containing photos : ")
    parent_folder = (
        r"C:\Users\Pablo\Desktop\230421 - goofy TU Delft LinkedIn ahh photos"
    )
    if parent_folder[0] == '"' and parent_folder[-1] == '"':
        parent_folder = parent_folder.strip('"')

    raw_photos_path = os.path.join(parent_folder, "raw")
    blacklist_txt_path = os.path.join(raw_photos_path, "blacklist.txt")
    raw_subfolders = [
        f.path for f in os.scandir(raw_photos_path) if f.is_dir()
    ]  # list of subfolders inside raw folder (one for each extension)

    selected_photos_path = os.path.join(parent_folder, "selected")
    whitelist_txt = os.path.join(selected_photos_path, "whitelist.txt")

    blacklist = photos_from_txt(blacklist_txt_path)
    remove_raw(raw_photos_path, blacklist)
