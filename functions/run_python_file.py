import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
  try:
      full_path = os.path.join(working_directory, file_path)
      absolute_full_path = os.path.abspath(full_path)
      absolute_working_directory = os.path.abspath(working_directory)
      if not absolute_full_path.startswith(absolute_working_directory):
          return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
      if not os.path.isfile(absolute_full_path):
          return f'Error: File "{file_path}" not found.'
      if not absolute_full_path.endswith('.py'):
          return f'Error: "{file_path}" is not a Python file.'
      result = subprocess.run(
          ["python", absolute_full_path, *args],
          cwd=absolute_working_directory,
          capture_output=True, text=True, timeout=30
      )

      output_parts = []
      if result.stdout:
          output_parts.append(f'STDOUT: {result.stdout}')
      if result.stderr:
          output_parts.append(f'STDERR: {result.stderr}')
      if result.returncode != 0:
          output_parts.append(f'Process exited with code {result.returncode}')

      if not output_parts:
          return "No output produced."
      return "\n".join(output_parts)

  except Exception as e:
      return f'Error: executing Python file: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Arguments to pass to the Python file.",
                ),
            ),
        },
        required=["file_path"],
    ),
)
