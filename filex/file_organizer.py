# standard library imports
import os
import shutil


from .exceptions import InvalidFolderPathError


class FileOrganizer:
    """
    A class for organizing files based on their extensions.
    """

    def __init__(self,folder_path):
        self.folder_path = folder_path

    def is_folder_path(self,path):
        """
        Check whether the given path is a folder or not.
        Args:
            path (str): The path to check.
        Raises:
            InvalidFolderPathError: If the path is not a valid folder.
        """
        if not os.path.isdir(path):
            raise InvalidFolderPathError("Invalid folder path")
    
    def  organize(self):
        """
        Organize files in the specified folder based on their extensions.
        """

        self.is_folder_path(self.folder_path)

        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)
            if os.path.isfile(file_path):
                extension = os.path.splitext(file)[1].lstrip(".")
                extension_path = os.path.join(self.folder_path, extension)
                if not os.path.exists(extension_path):
                    os.mkdir(extension_path)
                shutil.move(file_path, extension_path)
                print(f"File moved to ${extension_path} successfully")

            else:
                print(f"{file} not a file.Skipped")