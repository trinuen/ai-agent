import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
  try:
    working_dir_abs = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_file_path])
    
    if valid_target_dir != working_dir_abs:
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file_path):
      return f'Error: File not found or is not a regular file: "{target_file_path}"'
    
    with open(target_file_path, "r") as f: 
      content = f.read(MAX_CHARS)
      # After reading the first MAX_CHARS...
      if f.read(1):
          content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return content

  except Exception as e:
    return f"Error: reading files: {e}"