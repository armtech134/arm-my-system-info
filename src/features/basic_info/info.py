import win32api
import wmi

c = wmi.WMI()
my_os = c.Win32_OperatingSystem()[0]
info = [
  f"Computer Name: {win32api.GetComputerName()}",
  f"Username: {win32api.GetUserName()}",
  f"OS: {my_os.Caption} {my_os.Version} Build {my_os.BuildNumber}",
]
