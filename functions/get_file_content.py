import os

from google.genai import types

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_full_path = os.path.abspath(full_path)
        absolute_working_directory = os.path.abspath(working_directory)
        if not absolute_full_path.startswith(absolute_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(absolute_full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        if os.path.getsize(absolute_full_path) > MAX_CHARS:
            with open(absolute_full_path, 'r') as f:
                file_content = f.read(MAX_CHARS)
                file_content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        else:
            with open(absolute_full_path, 'r') as f:
                file_content = f.read()
        return file_content
    except Exception as e:
        return f'Error: {str(e)}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file relative to the working directory.",
            ),
        },
    ),
)
