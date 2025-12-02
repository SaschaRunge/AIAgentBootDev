import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory_path = os.path.abspath(os.path.join(working_directory, directory))

    if not os.path.isdir(abs_directory_path):
        return f'Error: "{directory}" is not a directory'
    if os.path.commonpath([abs_working_directory, abs_directory_path]) != abs_working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    result = ""

    try:
        with os.scandir(abs_directory_path) as dir_entries:
            for dir_entry in dir_entries:
                result += f"- {dir_entry.name}: file_size={dir_entry.stat().st_size} bytes, is_dir={dir_entry.is_dir()}\n"    
            return result
    except Exception as e:
        return f"Error: {directory} not found or inaccessible"

    
