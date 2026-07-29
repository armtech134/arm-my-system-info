import wmi


def get_disk_space_info():
  partitions = []
  try:
    c = wmi.WMI()
    for disk in c.Win32_LogicalDisk(DriveType=3):
      size = int(disk.Size) if disk.Size else 0
      free = int(disk.FreeSpace) if disk.FreeSpace else 0
      partitions.append({
        "device_id": disk.DeviceID,
        "file_system": disk.FileSystem,
        "size_bytes": size,
        "free_bytes": free,
        "used_bytes": size - free
      })
  except Exception:  # noqa: BLE001, S110
    pass
  return partitions
