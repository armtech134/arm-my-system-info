import re
import subprocess
import sys


def get_wmi_disk_wear(device_id):
  match = re.search(r"PHYSICALDRIVE(\d+)", device_id, re.IGNORECASE)
  if not match:
    return None

  disk_num = int(match.group(1))
  startupinfo = None
  if sys.platform == "win32":
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

  try:
    cmd = [
      "powershell",
      "-NoProfile",
      "-Command",
      f"Get-PhysicalDisk -DeviceNumber {disk_num} | Get-StorageReliabilityCounter | Select-Object -ExpandProperty Wear"
    ]
    res = subprocess.run(
      cmd,
      capture_output=True,
      text=True,
      startupinfo=startupinfo,
      check=False
    )
    if res.stdout:
      wear_str = res.stdout.strip()
      if wear_str.isdigit():
        return int(wear_str)
  except Exception:  # noqa: BLE001, S110
    pass
  return None
