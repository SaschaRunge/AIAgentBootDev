import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if os.path.commonpath([abs_working_directory, abs_file_path]) != abs_working_directory:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    dir_name = os.path.dirname(abs_file_path)
    relative_dir_name = os.path.dirname(os.path.relpath(abs_file_path, start=abs_working_directory))

    result = ""  
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
            result += f'Successfully created new directory {relative_dir_name}\n'
        except Exception as e:
            return f'Error: exception {e} occured while creating new directory {relative_dir_name}'
            
    try:
        with open(abs_file_path, "w") as file:
            file.write(content)       
        result += f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Could not write to "{file_path}", failed with exception: {e}'
    
    return result

