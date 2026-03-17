import os

def write_file(working_directory, file_path, content):
  try:
    working_dir_abs = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, abs_file_path])
    
    if valid_target_dir != working_dir_abs:
      return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abs_file_path):
      return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    os.makedirs(valid_target_dir, exist_ok=True)

    with open(abs_file_path, "w") as f:
      f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

  except Exception as e:
    return f"Error writing to file: {e}"