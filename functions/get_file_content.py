import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if os.path.commonpath([abs_working_directory, abs_file_path]) != abs_working_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    try:
        with open(abs_file_path, "r") as file:
            file_content = file.read()
            if len(file_content) > MAX_CHARS:
                return file_content[:MAX_CHARS + 1] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content
    except Exception as e:
        return f'Error: Cannot read "{file_path}". Reading the file returned the following exception: {e}'
    
