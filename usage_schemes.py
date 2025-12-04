from google.genai import types
from config import MAX_CHARS

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Read the contents of the specified file, up to a length of {MAX_CHARS} characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read from, relative to the working directory. Mandatory.",
            ),
        },
    ),
)


schema_get_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the python file specified. Accepts additional arguments as input.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to run, relative to the working directory. Mandatory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Optional command-line arguments that can be passed along to the specified file.",
            ),
        },
    ),
)


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the provided content to the specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write to, relative to the working directory. If the file already exists, its previous contents will be overwritten. Mandatory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the specified file. Mandatory.",
            ),
        },
    ),
)