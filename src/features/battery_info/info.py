import wmi


def get_battery_info():
  c = wmi.WMI()
  battery = c.Win32_Battery()[0]
  if not battery:
    return []
  else:
    info = [
      f"Name: {battery.Name}",
      f"Estimated Charge Remaining: {battery.EstimatedChargeRemaining} %",
    ]
    return info
