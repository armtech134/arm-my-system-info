import json


def extract_health_percentage(json_str):
  if not json_str:
    return None
  if json_str.startswith("ERROR:"):
    return json_str
  try:
    data = json.loads(json_str)

    # Check for access denied / open failed errors
    smartctl_info = data.get("smartctl", {})
    is_admin_user = False
    try:
      import ctypes
      is_admin_user = ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:  # noqa: BLE001, S110
      pass

    for msg in smartctl_info.get("messages", []):
      msg_str = msg.get("string", "")
      if "Error=5" in msg_str or "Open failed" in msg_str or "Unable to detect device type" in msg_str:
        if not is_admin_user:
          return "Admin Rights Required"
        else:
          return "Detection Failed"

    # 1. Try NVMe SSD health
    nvme_log = data.get("nvme_smart_health_information_log")
    if nvme_log:
      percentage_used = nvme_log.get("percentage_used")
      available_spare = nvme_log.get("available_spare")
      health_values = []
      if percentage_used is not None:
        health_values.append(max(0, 100 - int(percentage_used)))
      if available_spare is not None:
        health_values.append(int(available_spare))
      if health_values:
        return f"{min(health_values)}%"

    # 2. Try SATA SSD health attributes
    ata_attrs = data.get("ata_smart_attributes")
    if ata_attrs and "table" in ata_attrs:
      health_values = []
      for attr in ata_attrs["table"]:
        attr_id = attr.get("id")
        attr_name = attr.get("name", "").lower()
        value = attr.get("value")
        if value is not None and (attr_id in (231, 202, 233, 177, 232) or any(k in attr_name for k in ["life_left", "lifetime_remaining", "wearout", "wear_leveling", "available_reserv", "available_spare", "spare_blocks"])):
          health_values.append(int(value))
      if health_values:
        return f"{min(health_values)}%"

    # 3. Check overall SMART status if no percentage attribute is found
    smart_status = data.get("smart_status")
    if smart_status and "passed" in smart_status:
      return "100% (Passed)" if smart_status["passed"] else "0% (Failed)"

  except (json.JSONDecodeError, TypeError, ValueError, KeyError):
    pass
  return "Unknown"
