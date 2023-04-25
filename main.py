import os
import shutil

#TODO: implement creating subfolders in whitelist.txt using /foldername headers
#TODO: restructure everything into a class
#TODO: create rough GUI
#TODO: input any file name (maybe smth like: prefix: ____, identifier:____, postfix:____, e.g. prefix: "_IMG_", identifier: "nmber", postfix:"")
###CREATE FOLDERS THAT WILL CONTAIN ALL PHOTOS###
def create_template(
    root_path=r"C:\Users\Pablo\OneDrive - Delft University of Technology\fotacas",
    extension_list=[".cr2", ".jpg"],
):
    # give name to folder
    main_folder_path = os.path.join(root_path, input("What is the name of the folder?"))
    # change extensions if necessary
    flag = input("Do you want to change the default extensions? (.cr2,.jpg) [Y/N] ")
    if flag == "Y":
        extension_list = input(
            "Input all the extensions separated by a comma (e.g. .jpg,.png): "
        ).split(",")
    # create a raw folder and a selected folder for each extension
    for extension in extension_list:
        raw_folder = os.path.join(main_folder_path, extension, "raw")
        os.makedirs(raw_folder, exist_ok=True)
        selected_folder = os.path.join(main_folder_path, extension, "selected")
        os.makedirs(selected_folder, exist_ok=True)
    # create blacklist and whitelist files
    f = open(os.path.join(main_folder_path, "blacklist.txt"), "w")
    f = open(os.path.join(main_folder_path, "whitelist.txt"), "w")
    return main_folder_path, extension_list


###CREATE LIST FROM TXT FILE###
def photos_from_txt(txt_path):
    photos_list=[]
    # open file and get the img names into a list
    with open(txt_path, "r") as f:
        for line in f:
            print(line)
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
def remove_raw(main_folder_path, photos_list, extension_list=[".cr2", ".jpg"]):
    for extension in extension_list:  # loop all photo extensions
        for photo in photos_list:  # loop through all blacklisted photos
            try:
                os.remove(
                    os.path.join(
                        main_folder_path,
                        extension,
                        "raw",
                        f"{photo}{extension}",
                    )  # remove photos: main_folder\.extension\raw\photo_number.extension
                    # e.g.: C:\Users\Desktop\2021 photos\.jpg\raw\IMG_101.jpg
                )
                print(f"Deleted {photo}{extension}")
            except FileNotFoundError:
                print(f"File {photo}{extension} was already deleted!")


###MOVE SELECTED PHOTOS TO "SELECTED" FOLDER###
def move_selected(
    main_folder_path,
    photos_list: list, #must be whitelist
    extension_list=[".cr2", ".jpg"],
):
    for extension in extension_list: #loop through all extensions
        raw_subfolder_path= os.path.join(main_folder_path,extension,"raw")
        selected_subfolder_path = os.path.join(main_folder_path,extension,"selected")
        for photo in photos_list: #loop through all photos to copy
            try:
                photo_path = os.path.join(raw_subfolder_path,f"{photo}{extension}")
                shutil.copy(photo_path,selected_subfolder_path) #copy from raw folder to selected folder
            except FileNotFoundError:
                print(f"File {photo}{extension} does not exist")

if __name__ == "__main__":
    # parent_folder = input("Path of the folder containing photos : ")
    main_folder = (
        r"C:\Users\Pablo\Desktop\230421 - goofy TU Delft LinkedIn ahh photos"
    )
    if main_folder[0] == '"' and main_folder[-1] == '"':
        main_folder = main_folder.strip('"')
    blacklist_txt_path = os.path.join(main_folder, "blacklist.txt")
    whitelist_txt_path = os.path.join(main_folder,"whitelist.txt")

    whitelist = photos_from_txt(whitelist_txt_path)

    blacklist = photos_from_txt(blacklist_txt_path)
    print(blacklist)
    print(whitelist)
    remove_raw(main_folder, blacklist)
    move_selected(main_folder, whitelist)

    # parent_folder = (
    #     r"C:\Users\Pablo\Desktop\230421 - goofy TU Delft LinkedIn ahh photos"
    # )
    # raw_photos_path = os.path.join(parent_folder, "raw")

    # subfolders_path = [f.path for f in os.scandir(raw_photos_path) if f.is_dir()]
    # print(subfolders_path)
    # aa = os.path.join(subfolders_path, "hola")
    # print(aa)
    # main_folder_path, extension_list = create_template()
