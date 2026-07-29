from PySide6.QtWidgets import QVBoxLayout, QWidget

from features.disk_info.info import get_disk_info
from shared.widgets import ListView


class DiskInfoList(QWidget):
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout(self)
    layout.addWidget(ListView(label="Disk Info", items=get_disk_info()))
