import shutil
from sys import argv
from pathlib import Path

def main():
    args = get_arguments()
    if args:
        source, destination = args
        print(f"Starting copy from {source} to {destination}...")

        create_directory(destination)

        read_directory(source, destination)
        print("Done!")


def get_arguments():
    try:
        _, source, *rest = argv
        source = Path(source)
    except ValueError:
        print("Error: source path is required")
        return None

    try:
        destination = Path(rest[0])
    except IndexError:
        destination = Path("dist")

    if not source.exists():
        print("Error: source path does not exist")
        return None

    return source, destination


def read_directory(source_path, destination_path):
    try:
        for child in source_path.iterdir():
            if child.is_dir():
                read_directory(child, destination_path)
            else:
                copy_file(child, destination_path)
    except PermissionError:
        print(f"Permission denied: {source_path}")


def create_directory(destination_path):
    destination_path.mkdir(parents=True, exist_ok=True)
    return destination_path


def copy_file(source_path, destination_path):
    extension = source_path.suffix[1:].lower() or "others"

    extension_directory = destination_path / extension
    create_directory(extension_directory)

    try:
        shutil.copy2(source_path, extension_directory / source_path.name)
    except Exception as e:
        print(f"Error: error copying {source_path.name}: {e}")


if __name__ == "__main__":
    main()