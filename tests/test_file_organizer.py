import unittest
import os
import shutil
from filex.file_organizer import FileOrganizer 
from filex.exceptions import InvalidFolderPathError

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = "temp_test_dir"
        os.makedirs(self.temp_dir, exist_ok=True)
        for ext in ["txt", "jpg", "pdf"]:
            os.makedirs(os.path.join(self.temp_dir, ext), exist_ok=True)

    def tearDown(self):
        # Remove the temporary directory after testing
        shutil.rmtree(self.temp_dir)

    def test_valid_folder_path(self):
        organizer = FileOrganizer(self.temp_dir)
        self.assertIsNone(organizer.is_folder_path(self.temp_dir))

    def test_invalid_folder_path(self):
        organizer = FileOrganizer("nonexistent_folder")
        with self.assertRaises(InvalidFolderPathError):
            organizer.is_folder_path(self.temp_dir)

    def test_organize_files(self):
        organizer = FileOrganizer(self.temp_dir)

        # Create test files in the root folder
        for ext in ["txt", "jpg", "pdf"]:
            with open(os.path.join(self.temp_dir, f"file.{ext}"), "w") as f:
                f.write("Test content")

        organizer.organize()

        # Verify that files have been organized
        for ext in ["txt", "jpg", "pdf"]:
            self.assertTrue(os.path.exists(os.path.join(self.temp_dir, ext, f"file.{ext}")))

if __name__ == "__main__":
    unittest.main()
