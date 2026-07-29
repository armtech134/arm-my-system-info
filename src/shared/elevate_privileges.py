import ctypes
import sys


def elevate_privileges():
  try:
    if ctypes.windll.shell32.IsUserAnAdmin():
      return True
  except Exception:  # noqa: BLE001, S110
    pass

  # Prepare the script path and its arguments
  import os
  abs_argv = [os.path.abspath(arg) if i == 0 else arg for i, arg in enumerate(sys.argv)]
  params = " ".join([f'"{arg}"' for arg in abs_argv])

  try:
    # Relaunch the Python interpreter with administrator rights (runas verb)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
  except Exception:  # noqa: BLE001, S110
    pass

  sys.exit(0)
