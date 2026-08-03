import wmi


def get_battery_capacities():
  try:
    w = wmi.WMI(namespace="wmi")
    static_data = w.BatteryStaticData()
    full_charged_data = w.BatteryFullChargedCapacity()
    if static_data and full_charged_data:
      designed_capacity = static_data[0].DesignedCapacity
      full_charged_capacity = full_charged_data[0].FullChargedCapacity
      return designed_capacity, full_charged_capacity
  except Exception:  # noqa: BLE001, S110
    pass
  return None, None
