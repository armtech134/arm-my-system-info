import wmi

from features.battery_info.calculate_battery_health import calculate_battery_health
from features.battery_info.get_battery_capacities import get_battery_capacities


def get_battery_info():
  c = wmi.WMI()
  batteries = c.Win32_Battery()
  if not batteries:
    return ["No battery detected"]
  
  battery = batteries[0]
  info = [
    f"Name: {battery.Name}",
    f"Estimated Charge Remaining: {battery.EstimatedChargeRemaining} %",
  ]

  designed_cap, full_charged_cap = get_battery_capacities()
  if designed_cap is not None:
    info.append(f"Design Capacity: {designed_cap} mWh")
  if full_charged_cap is not None:
    info.append(f"Full Charge Capacity: {full_charged_cap} mWh")

  health = calculate_battery_health(designed_cap, full_charged_cap)
  if health is not None:
    info.append(f"Battery Health: {health} %")

  return info
