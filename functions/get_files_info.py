import os

from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        absolute_full_path = os.path.abspath(full_path)
        absolute_working_directory = os.path.abspath(working_directory)
        if not absolute_full_path.startswith(absolute_working_directory):
            return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(absolute_full_path):
            return f'    Error: "{directory}" is not a directory'
        str_content = ""
        content = os.listdir(absolute_full_path)
        for item in content:
            item_path = os.path.join(absolute_full_path, item)
            str_content += f" - {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n"
        return str_content
    except Exception as e:
        return f'    Error: {str(e)}'

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
