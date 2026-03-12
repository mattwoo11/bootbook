import os
import subprocess
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
            name="run_python_file",
            description="Run Python files with optional arguments",
            parameters=types.Schema(
                required=["file_path"],
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="Path to the Python file to execute",
                    ),
                    "args": types.Schema(
                        type=types.Type.ARRAY,
                        items=types.Schema(type=types.Type.STRING),
                        description="optional command-line arguments to pass to the Python file",
                    ),
                },
            ),
        )


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if valid_target_dir is False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_dir.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_dir]

        if args is not None:
            command.extend(args)
        
        sub = subprocess.run(command, cwd=working_dir_abs, capture_output=True, timeout=30, text=True)
        if sub.returncode != 0:
            return f"Process exited with code {sub.returncode}"
        if not sub.stderr and not sub.stdout:
            return "No output produced"
        
        output = ""
        if sub.stdout:
            output += f"STDOUT: {sub.stdout}"
        if sub.stderr:
            output += f"STDERR: {sub.stderr}"
        return output
    
    except Exception as e:
        return f"Error: {e}"