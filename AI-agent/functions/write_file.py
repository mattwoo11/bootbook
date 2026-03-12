import os
from google.genai import types


schema_write_file = types.FunctionDeclaration(
            name="write_file",
            description="Write or overwrite files",
            parameters=types.Schema(
                required=["file_path", "content"],
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="path to the file to write",
                    ),
                    "content": types.Schema(
                        type=types.Type.STRING,
                        description="content to write to the file",
                    ),
                },
            ),
        )


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        
        if valid_target_dir is False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        parent = os.path.dirname(target_dir)
        os.makedirs(parent, exist_ok=True)

        with open(target_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"