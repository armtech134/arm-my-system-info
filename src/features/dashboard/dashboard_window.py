from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from features.basic_info.basic_info_list import BasicInfoList
from features.disk_info import DiskInfoList
from features.ram_info import RamInfoList


class DashboardWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My System Info")
    container = QWidget()
    layout = QVBoxLayout(container)
    layout.addWidget(BasicInfoList())
    layout.addWidget(RamInfoList())
    layout.addWidget(DiskInfoList())
    self.setCentralWidget(container)


