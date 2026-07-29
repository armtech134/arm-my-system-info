import wmi

from features.disk_info.extract_health_percentage import extract_health_percentage
from features.disk_info.get_disk_space_info import get_disk_space_info
from features.disk_info.run_smartctl import run_smartctl


def get_disk_info():
  c = wmi.WMI()
  info = []

  try:
    info.append("Physical Drives Health:")
    for drive in c.Win32_DiskDrive():
      device_id = drive.DeviceID
      model = drive.Model

      json_output = run_smartctl(device_id)
      health = extract_health_percentage(json_output)

      info.append(f"  {device_id} ({model}): {health}")
  except Exception:  # noqa: BLE001, S110
    pass

  info.append("")

  try:
    info.append("Logical Partitions Space:")
    for disk in get_disk_space_info():
      device_id = disk["device_id"]
      file_system = disk["file_system"]
      size_gb = disk["size_bytes"] / (1024 * 1024 * 1024)
      used_gb = disk["used_bytes"] / (1024 * 1024 * 1024)
      free_gb = disk["free_bytes"] / (1024 * 1024 * 1024)

      info.append(f"  Drive {device_id} ({file_system}):")
      info.append(f"    Total: {size_gb:.2f} GB")
      info.append(f"    Used: {used_gb:.2f} GB")
      info.append(f"    Free: {free_gb:.2f} GB")
  except Exception:  # noqa: BLE001, S110
    pass

  return info
