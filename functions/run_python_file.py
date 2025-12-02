import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    path = os.path.join(working_directory, file_path)
    relative_path = os.path.relpath(path, working_directory)
    abs_path = os.path.abspath(path)

    if ".." in relative_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try: 
        completed_process = subprocess.run(f"python {path} {' '.join(args)}", timeout=30, shell=True)

        return_string = (
            f"STDOUT: {completed_process.stdout}\n"
            f"STDERR: {completed_process.stderr}"
        )

        if completed_process.returncode != 0:
            return_string += f"\nProcess exited with code {completed_process.returncode}"
        
        return return_string if len(return_string) != 0 else "No output produced"
    except Exception as e:
        return f"Error: executing Python file: {e}"




