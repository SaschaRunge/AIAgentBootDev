import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    if args is None:
        args = []
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if os.path.commonpath([abs_working_directory, abs_file_path]) != abs_working_directory:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try: 
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        completed_process = subprocess.run(
            commands, 
            timeout=30, 
            capture_output=True,
            text=True,
            cwd=abs_working_directory
        )

        return build_return_string(completed_process.stdout, completed_process.stderr, completed_process.returncode)

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
def build_return_string(stdout, stderr, returncode):
    return_string = ""

    if stdout:
        return_string += f"STDOUT:\n{stdout}\n"
    if stderr:
        return_string += f"STDERR:\n{stderr}\n"
    if returncode:
        return_string += f"Process exited with code {returncode}"
    return return_string if return_string else "No output produced"
    

 


