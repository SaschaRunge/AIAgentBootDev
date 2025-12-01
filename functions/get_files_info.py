import os

def get_files_info(working_directory, directory="."):
    path = os.path.join(working_directory, directory)
    relative_path = os.path.relpath(path, working_directory)

    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    if ".." in relative_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    result = ""

    try:
        dir_entries = os.scandir(path)
        for dir_entry in dir_entries:
            result += f"- {dir_entry.name}: file_size={dir_entry.stat().st_size} bytes, is_dir={dir_entry.is_dir()}\n"    
        return result
    except Exception as e:
        return f"Error: {directory} not found or inaccessible"

    
