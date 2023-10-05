import os
import shutil


class InvalidFolderPathError(Exception):
    """
    This exception will be raised if the folder
    path the user enters is incorrect
    """


def is_folder_path(path):
    """
    Check whether the path the user enters is a folder or not
    """
    if not os.path.isdir(path):
        raise InvalidFolderPathError("Invalid folder path")


LOOP = True

while LOOP:
    folder_path = input("Enter folder path: ")
    folder_path = folder_path.strip(" ")

    try:
        is_folder_path(folder_path)
        print("Valid folder path!")
        LOOP = False
    except InvalidFolderPathError as e:
        print(e)


for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lstrip(".")
        extension_path = os.path.join(folder_path, extension)
        if os.path.exists(extension_path):
            shutil.move(file_path, extension_path)
        else:
            os.mkdir(extension_path)
            shutil.move(file_path, extension_path)
        print(f"File moved to ${extension_path} successfully")
