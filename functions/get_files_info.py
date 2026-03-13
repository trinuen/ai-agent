import os

def get_files_info(working_directory, directory="."):
  try:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir])

    if valid_target_dir != working_dir_abs:
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
      return f'Error: "{directory}" is not a directory'

    contents = os.listdir(target_dir)
    files_info = []
    for content in contents:
      file = target_dir + "/" + content
      files_info.append(f"- {content}: file_size={os.path.getsize(file)} bytes, is_dir={os.path.isdir(file)}")
    return "\n".join(files_info)

  except Exception as e:
    return "Error: listing files: {e}"