import subprocess
import sys

from features.disk_info.find_smartctl import find_smartctl
from features.disk_info.get_smartctl_device_path import get_smartctl_device_path


def run_smartctl(device_id, model=None):
  smartctl_bin = find_smartctl()
  dev_path = get_smartctl_device_path(device_id)
  startupinfo = None
  if sys.platform == "win32":
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

  try:
    is_nvme = model and "nvme" in model.lower()

    if is_nvme:
      result = subprocess.run(
        [smartctl_bin, "-a", "-j", "-d", "nvme", dev_path],
        capture_output=True,
        text=True,
        startupinfo=startupinfo,
        check=False
      )
      if result.stdout and "nvme_smart_health_information_log" in result.stdout:
        return result.stdout

    result = subprocess.run(
      [smartctl_bin, "-a", "-j", dev_path],
      capture_output=True,
      text=True,
      startupinfo=startupinfo,
      check=False
    )

    if result.stdout and "Unable to detect device type" in result.stdout:
      result_sat = subprocess.run(
        [smartctl_bin, "-a", "-j", "-d", "sat", dev_path],
        capture_output=True,
        text=True,
        startupinfo=startupinfo,
        check=False
      )
      if result_sat.stdout and "Unable to detect device type" not in result_sat.stdout:
        return result_sat.stdout
    return result.stdout
  except Exception as e:  # noqa: BLE001
    return f"ERROR: {type(e).__name__}: {e!s}"
