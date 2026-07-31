import re


def get_smartctl_device_path(device_id):
  match = re.search(r"PHYSICALDRIVE(\d+)", device_id, re.IGNORECASE)
  if match:
    drive_num = int(match.group(1))
    return f"/dev/pd{drive_num}"
  return device_id
