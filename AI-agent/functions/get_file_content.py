import os
from config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
            name="get_file_content",
            description="Read the file contents",
            parameters=types.Schema(
                required=["file_path"],
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="path to the file to read",
                    ),
                },
            ),
        )


def get_file_content(working_directory, file_path):
    try:
        working_abs = os.path.abspath(working_directory)
        tar_dir = os.path.normpath(os.path.join(working_abs, file_path))
        valid_target_dir = os.path.commonpath([working_abs, tar_dir]) == working_abs
        if valid_target_dir is False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(tar_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(tar_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"