import argparse
from filex.file_organizer import FileOrganizer

def main():
    parser = argparse.ArgumentParser(description='Organize files based on their extensions.')
    parser.add_argument('-s', help='Source directory containing files to organize.')
    parser.add_argument('-d', help='Destination directory for organized files.')

    args = parser.parse_args()

    # Call your package's function to organize files
    organizer = FileOrganizer(folder_path=args.p)
    organizer.organize()

if __name__ == '__main__':
    main()