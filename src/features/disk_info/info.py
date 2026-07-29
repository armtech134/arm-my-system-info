import wmi


def get_disk_info():
  c = wmi.WMI()
  info = []

  try:
    info.append("Physical Drives Health:")
    for drive in c.Win32_DiskDrive():
      device_id = drive.DeviceID
      model = drive.Model
      status = drive.Status
      info.append(f"  {device_id} ({model}): {status}")
  except Exception:
    pass

  info.append("")

  try:
    info.append("Logical Partitions Space:")
    for disk in c.Win32_LogicalDisk(DriveType=3):
      device_id = disk.DeviceID
      size_gb = int(disk.Size) / (1024 * 1024 * 1024) if disk.Size else 0
      free_gb = int(disk.FreeSpace) / (1024 * 1024 * 1024) if disk.FreeSpace else 0
      used_gb = size_gb - free_gb
      file_system = disk.FileSystem
      info.append(f"  Drive {device_id} ({file_system}):")
      info.append(f"    Total: {size_gb:.2f} GB")
      info.append(f"    Used: {used_gb:.2f} GB")
      info.append(f"    Free: {free_gb:.2f} GB")
  except Exception:
    pass

  return info

