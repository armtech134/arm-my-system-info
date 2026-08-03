import platform
import win32api
import wmi


def get_basic_info():
  c = wmi.WMI()
  my_os = c.Win32_OperatingSystem()[0]
  system_info = c.Win32_ComputerSystem()[0]
  processors = c.Win32_Processor()
  processor_name = processors[0].Name if processors else "Unknown"
  is_x64 = "Yes" if platform.machine() in ("AMD64", "x86_64") else "No"

  role_map = {
    0: "Unspecified",
    1: "Desktop",
    2: "Mobile",
    3: "Workstation",
    4: "Enterprise Server",
    5: "SOHO Server",
    6: "Appliance PC",
    7: "Performance Server",
    8: "Slate",
  }
  platform_role = role_map.get(system_info.PCSystemType, "Unknown")

  return [
    f"Computer Name: {win32api.GetComputerName()}",
    f"Username: {win32api.GetUserName()}",
    f"OS: {my_os.Caption} {my_os.Version} Build {my_os.BuildNumber}",
    f"System Manufacturer: {system_info.Manufacturer}",
    f"System Model: {system_info.Model}",
    f"Platform Role: {platform_role}",
    f"Processor: {processor_name}",
    f"Is X64 Bit Device: {is_x64}",
  ]
