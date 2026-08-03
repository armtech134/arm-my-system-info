def calculate_battery_health(designed_capacity, full_charged_capacity):
  if not designed_capacity or not full_charged_capacity:
    return None
  try:
    if designed_capacity > 0:
      return round((full_charged_capacity / designed_capacity) * 100, 2)
  except Exception:  # noqa: BLE001, S110
    pass
  return None
