import wmi

from features.disk_info.extract_health_percentage import extract_health_percentage
from features.disk_info.get_disk_space_info import get_disk_space_info
from features.disk_info.get_wmi_disk_wear import get_wmi_disk_wear
from features.disk_info.run_smartctl import run_smartctl


def get_disk_info():
  c = wmi.WMI()
  info = []

  try:
    info.append("Physical Drives Health:")
    for drive in c.Win32_DiskDrive():
      device_id = drive.DeviceID
      model = drive.Model

      json_output = run_smartctl(device_id, model)
      health = extract_health_percentage(json_output)

      if health in ("Unknown", "Detection Failed", None):
        wear_val = get_wmi_disk_wear(device_id)
        if wear_val is not None:
          health = f"{max(0, 100 - wear_val)}%"
        else:
          wmi_status = getattr(drive, "Status", "Unknown")
          if wmi_status == "OK":
            health = "Healthy (WMI)"
          elif wmi_status == "Pred Fail":
            health = "Warning (Predicting Failure)"
          else:
            health = f"{wmi_status} (WMI)"

      info.append(f"  {device_id} ({model}): {health}")
  except Exception:  # noqa: BLE001, S110
    pass


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
