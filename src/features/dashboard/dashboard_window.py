from PySide6.QtWidgets import QMainWindow, QTabWidget

from features.basic_info.basic_info_list import BasicInfoList
from features.battery_info import BatteryInfoList
from features.disk_info import DiskInfoList
from features.ram_info import RamInfoList


class DashboardWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My System Info")

    tabs = QTabWidget()
    tabs.addTab(BasicInfoList(), "Basic &Info")
    tabs.addTab(RamInfoList(), "&RAM Info")
    tabs.addTab(DiskInfoList(), "&Disk Info")
    tabs.addTab(BatteryInfoList(), "&Battery Info")

    self.setCentralWidget(tabs)

