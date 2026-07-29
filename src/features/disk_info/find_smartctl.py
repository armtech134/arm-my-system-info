import os


def find_smartctl():
  base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
  local_path = os.path.join(base_dir, "bin", "smartctl.exe")
  if os.path.exists(local_path):
    return local_path
  return "smartctl"
