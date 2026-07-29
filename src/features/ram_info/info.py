import wmi


def get_ram_info():
  c = wmi.WMI()
  info = []

  try:
    os_info = c.Win32_OperatingSystem()[0]
    total_kb = int(os_info.TotalVisibleMemorySize)
    free_kb = int(os_info.FreePhysicalMemory)
    total_gb = total_kb / (1024 * 1024)
    free_gb = free_kb / (1024 * 1024)
    used_gb = total_gb - free_gb
    info.append(f"Total Memory: {total_gb:.2f} GB")
    info.append(f"Used Memory: {used_gb:.2f} GB")
    info.append(f"Free Memory: {free_gb:.2f} GB")
  except Exception:
    pass

  try:
    memory_modules = c.Win32_PhysicalMemory()
    for index, module in enumerate(memory_modules, start=1):
      capacity_gb = int(module.Capacity) / (1024 * 1024 * 1024)
      speed = getattr(module, "Speed", "Unknown")
      info.append(f"Module {index}: {capacity_gb:.2f} GB @ {speed} MHz")
  except Exception:
    pass

  return info
