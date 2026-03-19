import os
from config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get file content in a specified working directory, providing at most 10000 chars of the file, will end with '[...File {file_path} truncated at {MAX_CHARS} characters]' if file has more than 10000 chars",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path to read content from, relative to the working directory",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
  try:
    working_dir_abs = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, abs_file_path])
    
    if valid_target_dir != working_dir_abs:
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
      return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(abs_file_path, "r") as f: 
      content = f.read(MAX_CHARS)
      # After reading the first MAX_CHARS...
      if f.read(1):
          content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return content

  except Exception as e:
    return f"Error reading file: {e}"